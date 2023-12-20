## john the ripper

### zip brute force encrypted zips with

Convert the zip file to a hash using JohnTheRipper tool:
```bash
zip2john backup.zip > backup.hash
```
Use JohnTheRipper tool to hack the hash file:
```bash
$ john --wordlist=/usr/share/wordlists/rockyou.txt backup.hash

Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
741852963        (backup.zip)     
1g 0:00:00:00 DONE (2023-11-03 21:09) 100.0g/s 13107Kp/s 13107Kc/s 13107KC/s 123456..kovacs
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
```
the password is `741852963` in this case