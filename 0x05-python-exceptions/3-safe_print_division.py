#!/usr/bin/python3

def safe_print_division(a, b):
    div = None
    try:
        div = a / b
        print("Inside result: {:.1f}".format(div))
    except ZeroDivisionError:
        print("Inside result: {}".format(div))
    finally:
        return div
