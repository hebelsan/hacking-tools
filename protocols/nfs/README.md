## nfs 

runs on port 2049/tcp in combination with rpc like in this nmap output:
```bash
111/tcp  open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      40539/tcp   mountd
|   100005  1,2,3      46865/udp6  mountd
|   100005  1,2,3      54950/udp   mountd
|   100005  1,2,3      59903/tcp6  mountd
|   100021  1,3,4      37203/tcp   nlockmgr
|   100021  1,3,4      41095/udp   nlockmgr
|   100021  1,3,4      46299/tcp6  nlockmgr
|   100021  1,3,4      54201/udp6  nlockmgr
|   100024  1          36228/udp6  status
|   100024  1          44690/udp   status
|   100024  1          47445/tcp6  status
|   100024  1          59789/tcp   status
|   100227  3           2049/tcp   nfs_acl
|_  100227  3           2049/tcp6  nfs_acl
2049/tcp open  nfs_acl 3 (RPC #100227)
```

For more info: https://book.hacktricks.xyz/network-services-pentesting/nfs-service-pentesting

### check if share is available to mount

```bash
showmount -e <IP>
```
if available mount:

```bash
mkdir /tmp
mount -t nfs <IP>:/home /tmp
```