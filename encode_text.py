""" encode a string of text to md5 and sha message digest """
""" unicode objects must be encoded prior to being hashed """

import hashlib
from pyperclip import *

def encode_text_md5(string):
    output = hashlib.md5(string.encode()).hexdigest()
    return output

def encode_text_sha512(string):
    output = hashlib.sha512(string.encode()).hexdigest()
    return output

if __name__ == "__main__":
    while True:
        menu = '(1)\tmd5 encoding\n(2)\tsha 512 encoding'
        print(menu)
        choice = int(input('>: '))

        string = str(input('enter a string to encode: '))

        if len(string) > 20:
            print('encoding:', string[0:20])
        else:
            print('encoding:', string)

        if choice == 1:
            do = encode_text_md5(string)
            print(do)
            print()
            copy(do)
            print('encoding result copied to clipboard')
            
        elif choice == 2:
            do = encode_text_sha512(string)
            print(do)
            print()
            copy(do)
            print('encoding result copied to clipboard')
            
