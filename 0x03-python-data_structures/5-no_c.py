#!/usr/bin/python3

def no_c(my_string):
    table = str.maketrans('', '', 'Cc')
    new_string = my_string.translate(table)
    return new_string
