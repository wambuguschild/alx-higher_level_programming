#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys
    length = len(sys.argv)
    total = 0
    if length == 1:
        total = 0
    else:
        for i in range(1, length):
            total += int(sys.argv[i])
    print("{:d}".format(total))
