#!/usr/bin/python3
"""class to json module is here
"""


def class_to_json(obj):
	"""Returns a dict of class converted to json"""
	return obj.__dict__
