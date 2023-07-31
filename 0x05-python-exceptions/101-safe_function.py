#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """It will Execute a function safely.

    Args:
        fct: This is the function to be executed.
        args: This is the Arguments for fct.

    Returns:
        If there is an error that occurs - None.
        Otherwise - the result will be the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
