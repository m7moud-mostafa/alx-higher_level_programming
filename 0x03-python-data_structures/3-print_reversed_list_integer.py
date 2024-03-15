#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list.copy()
    new_list = new_list[::-1]
    for i in my_list[::-1]:
        print("{}".format(i))
