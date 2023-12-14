# Mysql

play with [sql queries](https://onecompiler.com/mysql)

## login

```bash
mysql -h localhost -u USER -p DB
```

## useful commands

```
SHOW TABLES;
```

## bypass parameter name checks

if for example it is not allowed to set the role parameter:

```php
foreach($_GET as $key=>$value) {
	if (strtolower($key) === 'role') {
		// prevent malicious users to modify role
		header('Location: /index.php?err=Malicious activity detected!');
		die;
	}
	$args[$key] = $value;
}
```

we can use a comment:

```
GET /save_game.php?clicks=4&level=0&role/**/=Admin
```
