#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if 97 <= ord(i) <= 122:
            a = chr(ord(i) - 32)
        else:
            a = i
        print("{}".format(a), end="")
    print()
