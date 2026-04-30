#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        i = my_list[0]
        for item in my_list[::-1]:
            if i < item:
                i = item
        return i
