#!/usr/bin/python3
"""This defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """It adds a new attribute to an object if possible.
    Args:
        obj (any): This is the object to add an attribute to.
        att (str): This is the name of the attribute to add to obj.
        value (any): This is the value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
