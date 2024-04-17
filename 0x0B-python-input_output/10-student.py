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
        if not attrs:
            return self.__dict__
        dic = {}
        for key in attrs:
            try:
                dic[key] = self.__dict__[key]
            except KeyError:
                pass
        return dic
