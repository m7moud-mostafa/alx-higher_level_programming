#!/usr/bin/python3
"""
This module related to json
"""


import json


def save_to_json_file(my_obj, filename):
    """Writs object to a text file using json representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
