#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximum = my_list[0]  # assume first is largest
    for i in my_list[1:]:
        if i > maximum:
            maximum = i   # found a bigger one
    return maximum
