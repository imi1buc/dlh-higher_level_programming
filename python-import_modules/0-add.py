#!/usr/bin/python3
with open("add_0.py") as f:
    exec(f.read())
a = 1
b = 2
print("{}".format(add(a, b)))
