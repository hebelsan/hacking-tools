## Linux
- check if secrets are in environment
> env or printenv

- check running processes
> ps aux

- check which bin user can run as sudo
```bash
sudo -l
# if `sudo -l` returns (ALL : ALL) ALL -> just run `sudo su` and you are root
# to remove users from sudo
sudo deluser USER sudo
# to check sudo rights for other users
sudo -l -U USER
```

- To find all suid (this means the file always runs under the user who owns the file, in this case root) files run: 
```bash
find / -perm -4000 2>/dev/null
```

- check those bins on gtfobins
> https://gtfobins.github.io/

- find all files in home directoy with nice print
```bash
find /home -type f -printf "%f\t%p\t%u\t%g\t%m\n" 2>/dev/null | column -t
```

- find all files belonging to user - filter and ignore errors
```bash
find / -user <USER> 2>/dev/null | grep -v '^/sys\|^/proc\|^/run'
```

- check if source code contains passwords, -i means ignore-case, -a handles binary like text files
```bash
cat * | grep -i -a passw*
# or
grep -r 'passw' .
```

- check kernel version (might is old and has CVE)
> uname -a

- check bash history in .bash_history

- find binary within a group
> uid=1000(robert) gid=1000(robert) groups=1000(robert),1001(bugtracker)  
> find / -group bugtracker 2>/dev/null

- `pspy` to do unprivileged Linux process snooping

- In case you can run any perl application as sudo check [perl startup privilege escalation](https://medium.com/@DGclasher/privilege-escalation-through-perl-environment-variables-349b39ca01)

- run linPEAS

## windows

- check the file `ConsoleHost_history.txt` which holds a history of recent Windows PowerShell commands executed

- run winPEAS

- all checks are explained here: https://book.hacktricks.xyz/windows-hardening/checklist-windows-privilege-escalation

- if credentials found run `psexec.py` from the Impacket suite to get a shell as the administrator
> impacket-psexec administrator@{TARGET_IP}

