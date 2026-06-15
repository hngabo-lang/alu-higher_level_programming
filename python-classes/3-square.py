#!/usr/bin/python3
"""Module that defines a Square class with an area method."""


class Square:
    """A class that defines a square with an area method."""

    def __init__(self, size=0):
        """Instantiate a Square with an optional size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
