#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """It Prints an integer with "{:d}".format().

    If there is a ValueError message that is caught, a corresponding
    message is printed to the standard error.

    Args:
        value (int): This is the integer to print.

    Returns:
        If there is a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
