#!/usr/bin/python3

def islower(c):
    ascii_value = ord(c)
    for i in range(97, 123):
        if i == ascii_value:
            return True
    return False
