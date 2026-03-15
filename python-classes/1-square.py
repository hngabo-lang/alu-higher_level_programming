#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """A class that defines a square by its private size."""

    def __init__(self, size):
        """Instantiate a Square with a given size."""
        self.__size = size
