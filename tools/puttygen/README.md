## puttygen

PuTTY doesn't natively support the private key format (.pem).

```bash
sudo apt-get install putty-tools
```

## convert .ppk to .pem

```bash
puttygen ppkkey.ppk -O private-openssh -o pemkey.pem
```

## convert .pem to .ppk

```bash
puttygen pemKey.pem -o ppkKey.ppk -O private
```