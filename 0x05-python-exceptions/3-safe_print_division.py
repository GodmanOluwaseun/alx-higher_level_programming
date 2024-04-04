#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        div = a / b
        print("{} / {} = {}".format(a, b, div))
        return
    except ZeroDivisionError:
        return None
    finally:
        print(f"Inside result: {div}")
