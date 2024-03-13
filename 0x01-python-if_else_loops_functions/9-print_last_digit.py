#!/usr/bin/python3

def print_last_digit(number):
    last_digit = number % 10

    if last_digit >= 0:
        pass
    else:
        last_digit = 10 - last_digit

    print("{}".format(last_digit))

    return last_digit