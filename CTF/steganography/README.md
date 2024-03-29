# steganography

Steganography is the practice of representing information within another message or physical object, in such a manner that the presence of the information is not evident to human inspection. In computing/electronic contexts, a computer file, message, image, or video is concealed within another file, message, image, or video.

## information vectors

- use `file` cli to check for real file type
- use `strings` cli to print out strings that are at least 4 characters long
- use `exiftool` cli to read metadata in images like author or gps data
- use `binwalk` cli to search for embedded files

## fix corrupted jpeg file
see jpeg header explanation: https://yasoob.me/posts/understanding-and-writing-jpeg-decoder-in-python/ and use hex editor to manipulate

## mp3
extract phone number in audio file: https://github.com/ribt/dtmf-decoder
-> after that probably use t9 decoder

## Polyglot
often pfd and png in one file.
use pdf ending and open with browser, then change to png and.