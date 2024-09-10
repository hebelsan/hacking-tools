# Cyberchef

Can automatically detect what kind of encryption is used: base64, hex, cesar... and decodes it 
https://gchq.github.io/CyberChef/

## cesar chiffre

- shift of the alphabet by a certain number

## base64

- sometimes double base64 decoded

## 32 bit little endian to big endian

From here, we notice that first 4 bytes, also the header signature seems to be reversed of a JPG header FF D8 FF E0 (JPG header) → E0 FF D8 FF, so every 4 bytes is flipped. Task: Flip back for every 4 bytes.
```bash
hexdump -v -e '1/4 "%08x"' challengefile | xxd -r -p > output_file
```
This command reads the contents of input_file in binary format and then converts it into hexadecimal format with each group of 4 bytes represented as an 8-character hexadecimal string.


## T9

- https://de.wikipedia.org/wiki/Text_on_9_keys  
- 22 33 8 8 33 777 222 2 88 555 7777 2 88 555 -> translates to "better*call*saul*"

## Morse

Text in the following pattern is Morse encoded:
```
.- / .--. .... --- -. . / .. ... / .... .. -.. -.. . -. / .. -. / - .... . / -.. .-. .- .-- . .-. / ..- -. -.. . .-. / - .... . / .-. .- -.. .. --- .-.-.-
 ```