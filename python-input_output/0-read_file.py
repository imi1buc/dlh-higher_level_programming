#!/usr/bin/python3
"""Reading a file"""


def read_file(filename=""):
    # Reading the file
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
