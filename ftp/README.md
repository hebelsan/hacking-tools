# ftp
https://book.hacktricks.xyz/network-services-pentesting/pentesting-ftp#anonymous-login

## anonymous login
check wrongly configured by trying these creds:
```bash
#anonymous : anonymous
#anonymous :
#ftp : ftp
ftp <IP>
>anonymous
>anonymous
>ls -a # List all files (even hidden) (yes, they could be hidden)
>bye #exit
```
> 