#!/usr/bin/python3
"""It Define a class Square."""


class Square:
    """It Represents a square."""

    def __init__(self, size=0):
        """It Initializes a new Square.

        Args:
            size (int): It is the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
