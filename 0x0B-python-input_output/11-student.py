#!/usr/bin/python3
"""This module contains the Student Class
"""


class Student:
    """
    Student Class contains the student name and age
    """
    def __init__(self, first_name, last_name, age):
        """Initializing the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict representation of Student instance"""
        if not isinstance(attrs, list) \
           or not all(isinstance(key, str) for key in attrs):
            return self.__dict__
        dic = {}
        for key in attrs:
            try:
                dic[key] = self.__dict__[key]
            except Exception as e:
                pass
        return dic

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
