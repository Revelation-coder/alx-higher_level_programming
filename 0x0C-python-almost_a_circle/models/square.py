#!/usr/bin/python3
"""Module documentation for Square class"""

from models.rectangle import Rectangle
import json
import csv


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overriding the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}

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
