# gobuster

https://github.com/OJ/gobuster

## directory search
```bash
gobuster dir -u https://example.com -w /wordlists/Discovery/Web-Content/common.txt -o gobuster-dirs.txt
```

## subdomain
```bash
# use vhost mode if inspecting not a real server but only over /etc/hosts
gobuster vhost --append-domain -u http://topology.htb -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-20000.txt -t 100 -o gobuster-subs.txt
# otherwise use dns mode
gobuster dns -d DOMAIN -t 100 -w subdomains-top1mil-20000.txt -o gobuster-subs.txt
```
