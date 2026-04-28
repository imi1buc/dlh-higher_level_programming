#!/usr/bin/python3
def no_c(my_string):
    result = "".join(str(i) for i in list(my_string) if i not in ('C', 'c'))
    return result
