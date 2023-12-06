## common nginx misconfigurations

[Hacking Tricks](https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/nginx)

### Missing root location

```nginx
server {
        root /etc/nginx;

        location /hello.txt {
                try_files $uri $uri/ =404;
                proxy_pass http://127.0.0.1:8080/;
        }
}
```

The root directive specifies the root folder for Nginx. In the above example, the root folder is /etc/nginx which means that we can reach files within that folder. The above configuration does not have a location for / (location / {...}), only for /hello.txt. Because of this, the root directive will be globally set, meaning that requests to / will take you to the local path /etc/nginx.   

A request as simple as GET /nginx.conf would reveal the contents of the Nginx configuration file stored in /etc/nginx/nginx.conf. If the root is set to /etc, a GET request to /nginx/nginx.conf would reveal the configuration file. In some cases it is possible to reach other configuration files, access-logs and even encrypted credentials for HTTP basic authentication.

### Off-By-Slash

```
server {
        listen 80 default_server;

        server_name _;

        location /static {
                alias /usr/share/nginx/static/;
        }

        location /api {
                proxy_pass http://apiserver/v1/;
        }
}
```

With the Off-by-slash misconfiguration, it is possible to traverse one step up the path due to a missing slash. Orange Tsai made this technique well known in his Blackhat talk “Breaking Parser Logic!” In this talk he showed how a missing trailing slash in the location directive combined with the alias directive can make it possible to read the source code of the web application. What is less well known is that this also works with other directives like proxy_pass. Let’s break down what is happening and why this works.

```
        location /api {
                proxy_pass http://apiserver/v1/;
        }
```

With an Nginx server running the following configuration that is reachable at server, it might be assumed that only paths under http://apiserver/v1/ can be accessed.

```
http://server/api/user -> http://apiserver/v1//user
```

When http://server/api/user is requested, Nginx will first normalize the URL. It then looks to see if the prefix /api matches the URL, which it does in this case. The prefix is then removed from the URL so the path /user is left. This path is then added to the proxy_pass URL which results in the final URL http://apiserver/v1//user. Note that there is a double slash in the URL since the location directive does not end in a slash and the proxy_pass URL path ends with a slash. Most web servers will normalize http://apiserver/v1//user to http://apiserver/v1/user, which means that even with this misconfiguration everything will work as expected and it could go unnoticed.

This misconfiguration can be exploited by requesting http://server/api../ which will result in Nginx requesting the URL http://apiserver/v1/../ that is normalized to http://apiserver/. The impact that this can have depends on what can be reached when this misconfiguration is exploited. It could for example lead to the Apache server-status being exposed with the URL http://server/api../server-status, or it could make paths accessible that were not intended to be publicly accessible.

One sign that a Nginx server has this misconfiguration is the server still returns the same response when a slash in the URL is removed. For example, if both http://server/api/user and http://server/apiuser return the same response, the server might be vulnerable. This would lead to the following requests being sent:

```
http://server/api/user -> http://apiserver/v1//user
http://server/apiuser -> http://apiserver/v1/user
```

See also https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/nginx#alias-lfi-misconfiguration
