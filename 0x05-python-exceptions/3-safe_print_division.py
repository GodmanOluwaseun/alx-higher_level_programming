#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
        return print("{} / {} = {}".format(a, b, div))
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(div))
