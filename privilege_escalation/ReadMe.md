- check if secrets are in environment
> env or printenv

- check which bin user can run as sudo
> sudo -l

- check thos bins on gtfobins
> https://gtfobins.github.io/

- find all files belonging to user - filter and ignore errors
> find / -user <USER> 2>/dev/null | grep -v '^/sys\|^/proc\|^/run'

- find all files in home directoy with nice print
> find /home -type f -printf "%f\t%p\t%u\t%g\t%m\n" 2>/dev/null | column -t

- check kernel version (might is old and has CVE)
> uname -a

