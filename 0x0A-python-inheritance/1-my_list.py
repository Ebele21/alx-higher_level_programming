#!/usr/bin/python3
"""
This contains the MyList class
"""


class MyList(list):
    """This a subclass of list"""
    def __init__(self):
        """It initializes the object"""
        super().__init__()

    def print_sorted(self):
        """It prints the sorted list"""
        print(sorted(self))
