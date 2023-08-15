#!/usr/bin/python3
"""
This Contains the clas "Student"
"""


class Student:
    """This is a Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """It Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """It returns a dictionary representation of a Student instance"""
        return self.__dict__
