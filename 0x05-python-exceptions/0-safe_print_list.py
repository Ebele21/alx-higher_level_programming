#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """It will Print x elements of a list.

    Args:
        my_list (list): It is the list to print elements from.
        x (int): It is the number of elements of my_list to print.

    Returns:
        The number of elements to be printed.
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
