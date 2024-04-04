#!/usr/bin/python3

def safe_print_division(a, b):
    div = None
    try:
        div = a / b
        print("{} / {} = {}".format(a, b, div))
        return div
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(div))
