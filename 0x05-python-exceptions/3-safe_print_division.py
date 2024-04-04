#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
        print("{:d}".format(div))
        return div
    except ZeroDivisionError:
        return None
    finally:
        print(f"Inside result: {div}")
