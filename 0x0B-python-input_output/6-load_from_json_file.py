#!/usr/bin/python3
"""
This module related to json
"""


import json


def load_from_json_file(filename):
    """Loads object from a text file using json representation"""
    with open(filename, "r") as f:
        return json.load(f)
