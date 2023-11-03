# General starting points

- scan open ports
```bash
mkdir nmap && nmap -sC -sV -oA nmap/scan 10.10.11.230
```

## webservice
- find hidden dirs with gobuster (use special wordlist if know which server e.g. spring):
```
gobuster dir -u https://www.test.com -w /usr/share/wordlists/big.txt
```
- enumerate subdomains with gobuster:
```
# for no real server vhost, for real use dns mode
gobuster vhost -u http://thetoppers.htb -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains.txt -t 100
```
- check website code html and javascript
- check if code xss is possible (command, sql or template injection)
> To identify SSTI: `${{<%[%'"}}%\.`  
> sql injection with sqlmap
- check versions of software and cve's
