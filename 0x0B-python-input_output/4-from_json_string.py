#!/usr/bin/python3
"""
This module related to json
"""


import json


def from_json_string(my_str):
    """Returns the json representation of an object"""
    return json.load(my_str)
