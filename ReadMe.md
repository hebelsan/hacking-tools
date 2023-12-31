# General starting points

- scan open ports
```bash
mkdir nmap && nmap -sC -sV -oA nmap/scan 10.10.11.230
```

## efficiency
when targeting multiple machines in network it may be wise to use a tool like `autorecon`

## web service
- find hidden dirs with [gobuster](./tools/gobuster/README.md) (use special wordlist if know which server e.g. spring) or file ending with -x php:
```
gobuster dir -u https://www.test.com -w /usr/share/wordlists/big.txt
```
- enumerate subdomains with gobuster, especially if website has already 1 subdomain there might be more:
```
# for no real server vhost, for real use dns mode
gobuster vhost -u http://thetoppers.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains.txt -t 100
```

- check website code html and javascript

- check if code xss is possible (command, sql or template injection)
> To identify SSTI: `${{<%[%'"}}%\.`  
> sql injection with sqlmap

- check versions of software and cve's

- check dirs, files and misconfigurations of a web server type e.g. [nginx](./webserver/nginx/README.md) or [apache2](./webserver/apache2/README.md) 

### web login

- try admin/admin or root/root

- check default login credentials for proprietary software!