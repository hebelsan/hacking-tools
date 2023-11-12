# put hashes with new line seperator in a file hashes.txt

# first identify the hash type with the first characters or use hashid

```bash
hashcat --help | grep -I '$2'
```

# with e.g. 3200 bcrypt blowfish unix

- --potfile-disabled: The potfile stores which hashes were already cracked, and thus won't be cracked again
```bash
hashcat -w 3200 hashes.txt rockyou.txt --potfile-disable
``````