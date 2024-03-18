#!/usr/bin/python3

def uppercase(str):
    chr_str = ""
    for i in range(0, len(str)):
        char_num = ord(str[i])
        if 97 <= char_num and char_num <= 122:
            char_num -= 32
            upper_char = chr(char_num)
            chr_str += upper_char
            continue
        chr_str += str[i]
    print(chr_str)
