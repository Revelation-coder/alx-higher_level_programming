#!/usr/bin/python3
"""This module defines a Rectangle class which is a sub class of Base class"""
from models.base import Base
import json
import csv


class Rectangle(Base):
    """A class representing a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle object"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the rectangle using the `#` character"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle attributes"""
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

    def update(self, *args, **kwargs):
        """Update the Rectangle instance attributes."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle instance."""
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string([obj.to_dictionary()
                                          for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects to a file in CSV format.

        Args:
            list_objs (list): A list of object instances.
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if isinstance(obj, Rectangle):
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif isinstance(obj, Square):
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """Load a list of objects from a CSV file.

        Returns:
            A list of object instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                list_objs = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(width=int(row[1]), height=int(row[2]),
                                  x=int(row[3]), y=int(row[4]), id=int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(size=int(row[1]), x=int(row[2]),
                                  y=int(row[3]), id=int(row[0]))
                    list_objs.append(obj)
                return list_objs
        except FileNotFoundError:
            return []
