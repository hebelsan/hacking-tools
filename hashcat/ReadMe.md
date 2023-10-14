# put hashes with new line seperator in a file hashes.txt

# first identify the hash type with the first characters
hashcat --help | grep -I '$2'

# with e.g. 3200 bcrypt blowfish unix
hashcat -w 3200 hashes.txt rockyou.txt --potfile-disable
