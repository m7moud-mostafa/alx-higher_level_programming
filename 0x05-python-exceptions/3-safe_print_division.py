#!/usr/bin/python3

def safe_print_division(a, b):
    div = None
    try:
        div = a / b
        print("Inside result: {:.1f}".format(div))
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(div))
        return div
