#!/usr/bin/python3
"""Deletes item at specific position in a list."""


def delete_at(my_list=[], idx=0):
    """Delete item at idx using del statement."""
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
