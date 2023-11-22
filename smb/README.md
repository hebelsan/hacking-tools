# info
runs on port 445 and 139

## enumerate the SMB with smbclient
```bash
smbclient -N -L \\\\{TARGET_IP}\\
-N : No password
-L : This option allows you to look at what services are available on a server
```

or with slightly different output:

```bash
# -u "guest" or empty
enum4linux -a -u "guest" -p "" 10.10.11.241
```

## list shares
```bash
smbclient -L \\\\10.129.112.234
```

## access share
```bash
smbclient \\\\10.129.112.234\\SHARE_NAME
```

## download file
```bash
smb: \> get {FILE}
```
