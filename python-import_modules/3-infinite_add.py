#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv[1:]
    total = 0
    for i, arg in enumerate(argv, 1):
        total += int(arg)
    print("{}".format(total))
