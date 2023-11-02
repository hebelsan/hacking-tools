## Linux
- check if secrets are in environment
> env or printenv

- check which bin user can run as sudo
> sudo -l

- check those bins on gtfobins
> https://gtfobins.github.io/

- find all files belonging to user - filter and ignore errors
> find / -user <USER> 2>/dev/null | grep -v '^/sys\|^/proc\|^/run'

- find all files in home directoy with nice print
> find /home -type f -printf "%f\t%p\t%u\t%g\t%m\n" 2>/dev/null | column -t

- check kernel version (might is old and has CVE)
> uname -a

- check bash history in .bash_history

- run linPEAS

## windows

- check the file `ConsoleHost_history.txt` which holds a history of recent Windows PowerShell commands executed

- run winPEAS

- all checks are explained here: https://book.hacktricks.xyz/windows-hardening/checklist-windows-privilege-escalation

- if credentials found run `psexec.py` from the Impacket suite to get a shell as the administrator
> impacket-psexec administrator@{TARGET_IP}

