#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.

    Args:
        my_list[list]: The list to print elemts from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of elements printed. -val
    """

    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print("")
    return (count)
