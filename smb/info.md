# info
runs on port 445

## list shares
smbclient -L \\\\10.129.112.234

## access share
smbclient \\\\10.129.112.234\\SHARE_NAME
