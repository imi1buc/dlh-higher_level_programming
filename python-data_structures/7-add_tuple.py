#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_list = []
    for i in range(0, 2):
        val_a = tuple_a[i] if i < len(tuple_a) else 0
        val_b = tuple_b[i] if i < len(tuple_b) else 0
        new_list.append(val_a + val_b)
    result = tuple(new_list)
    return result
