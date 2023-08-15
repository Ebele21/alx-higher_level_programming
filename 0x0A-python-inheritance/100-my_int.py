#!/usr/bin/python3
"""
It Contains the class MyInt
"""


class MyInt(int):
    """it is the rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """it creates a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """what was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """what was == is now !="""
        return int(self) == other
