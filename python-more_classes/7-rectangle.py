#!/usr/bin/python3
"""Module for Rectangle class"""


class Rectangle:
    """Class that defines a rectangle with print symbol"""

    number_of_instances = 0
    print_symbol = "#"

    def _init_(self, width=0, height=0):
        """Instantiation with optional width and height"""
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self._width * self._height

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def _str_(self):
        """Returns string representation with print_symbol"""
        if self._width == 0 or self._height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                result += "\n"
        return result

    def _repr_(self):
        """Returns official string representation"""
        return "Rectangle({}, {})".format(self._width, self._height)

    def _del_(self):
        """Prints message when instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
