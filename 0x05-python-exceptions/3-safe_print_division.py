#!/usr/bin/python3

def safe_print_division(a, b):
    """It Returns the division of a number a by another number b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
