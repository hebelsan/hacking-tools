# General starting points

- scan open ports
```bash
mkdir nmap && nmap -sC -sV -oA nmap/scan 10.10.11.230
```
- if webservice was found check hidden dirs with gobuster (use special wordlist if know which server e.g. spring)
```
gobuster dir -u https://www.test.com -w /usr/share/wordlists/big.txt
```
- check website code html and javascript
- check if code xss is possible (command, sql or template injection)
> To identify SSTI: `${{<%[%'"}}%\.`  
> sql injection with sqlmap
- check versions of software and cve's
