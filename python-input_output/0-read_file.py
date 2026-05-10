#!/usr/bin/python3
"""Reading a file"""


def read_file(filename=""):
    """Reads contents of a text file and print to stdout."""
    with open(filename, encoding='utf-8') as file:
        # This is the content
        print(file.read(), end='')
