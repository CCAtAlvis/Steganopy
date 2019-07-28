# SteganoPy
A steganographic library built on PIL (Pillow)

## Usage
Take an image, provide its path, put your data, And run the file... you have the steganographed image ready.

## Limitations
Currently only 1 byte of data is encoded per pixel. So you can only encode so much data as the total pixels of the image, viz length*height of the image. This can be improved by using stream encodig instead of block encoding and, later on, also data compression itself.

## TODO
- Convert stegano to proper class
- A simple key cipher
- Better usage of space by using 1 unused bit
- Compressing (probably simple Huffmann encoding) of the raw data
- Docs (whoever little maybe :p)
- Probably encrypt the data
