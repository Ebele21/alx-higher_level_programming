#!/usr/bin/python3
# 4-print_square.py
"""This Defines a square-printing function."""


def print_square(size):
    """It Prints a square with the # character.

    Args:
        size (int): It is the height/width of the square.
    Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
