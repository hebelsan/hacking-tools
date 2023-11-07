- general info https://book.hacktricks.xyz/network-services-pentesting/27017-27018-mongodb

- if connect fails check which port mongo is running on, then do `mongo --port 1234`

- to print nice json use `db.<Collection>.find().forEach(printjson);`

- update entry `db.Employee.update({"_id" : 1}, {$set: { "name" : "new"}});`