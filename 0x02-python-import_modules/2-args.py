#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    count = len(sys.argv)
    if count <= 1:
        print("0 arguments.")
    elif count == 2:
        print("{} argument:".format(count - 1))
    else:
        print("{} arguments:".format(count - 1))
    for i in range(1, count):
        print("{}: {}".format(i, sys.argv[i]))
