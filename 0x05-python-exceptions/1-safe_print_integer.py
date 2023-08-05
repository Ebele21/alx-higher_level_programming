#!/usr/bin/python3


def safe_print_integer(value):
    """It Prints an integer with "{:d}".format().

    Args:
        The value (int): Is the integer to print.

    Returns:
        If it is  a TypeError or ValueError that occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
