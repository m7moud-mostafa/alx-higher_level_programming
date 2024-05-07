#!/usr/bin/python3
"""This module contains the Base class"""
import json


class Base:
    """The Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json representation of list of dicts"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([])

    @classmethod
    def save_to_file(cls, list_objs):
        """saves json into file"""
        if list_objs is None:
            list_objs = []
        class_name = cls.__name__
        filename = class_name + ".json"
        objs_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(objs_dict)
        with open(filename, "w") as file:
            file.write(json_str)


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
