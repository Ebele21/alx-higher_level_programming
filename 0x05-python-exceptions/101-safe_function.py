#!/usr/bin/python3
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
        r = fct(*args)
        return r
    except Exception as error:
        import sys
        print("Exception: {}".format(error), file=sys.stderr)
        return None
