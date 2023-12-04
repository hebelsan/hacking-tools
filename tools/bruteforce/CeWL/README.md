## CeWL (cool)

CeWL is a wordlist generator that is unique compared to other tools available. While many tools rely on pre-defined lists or common dictionary attacks, CeWL creates custom wordlists based on web page content.

### customization

1. Specify spidering depth: The -d option allows you to set how deep CeWL should spider. For example, to spider two links deep: `cewl http://10.10.153.166 -d 2 -w output1.txt`
2. Set minimum and maximum word length: Use the `-m` and `-x` options respectively. For instance, to get words between 5 and 10 characters: `cewl http://10.10.153.166 -m 5 -x 10 -w output2.txt`
3. Handle authentication: If the target site is behind a login, you can use the `-a` flag for form-based authentication.
4. Custom extensions: The `--with-numbers` option will append numbers to words, and using `--extension` allows you to append custom extensions to each word, making it useful for directory or file brute-forcing.
5. Follow external links: By default, CeWL doesn't spider external sites, but using the `--offsite` option allows you to do so.

### examples

```bash
cewl -d 0 -m 5 -w usernames.txt http://10.10.153.166/team.php --lowercase
```

```bash
cewl -d 2 -m 5 -w passwords.txt http://10.10.153.166 --with-numbers
```