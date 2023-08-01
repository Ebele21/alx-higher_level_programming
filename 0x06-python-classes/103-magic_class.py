#!/usr/bin/python3
"""It Defines a MagicClass matching exactly a bytecode."""

import math

class MagicClass:
    """It Represents a circle."""

    def __init__(self, radius=0):
        """It Initializes a MagicClass.

        Arg:
            radius (float or int): It is the radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """It Returns the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """It Returns The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
