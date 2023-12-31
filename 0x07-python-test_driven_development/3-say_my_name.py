#!/usr/bin/python3
# 3-say_my_name.py
"""This Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """It Prints a name.

    Args:
        first_name (str): This is the first name to print.
        last_name (str): This is the last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
