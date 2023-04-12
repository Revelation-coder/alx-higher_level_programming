#!/usr/bin/python3
'''
class Student that defines a student
'''


class Student:
    '''
    module class student
    '''

    def __init__(self, first_name, last_name, age):
        '''method __init__
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = agei
   
     def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.
        :param attrs: A list of attributes to retrieve.
        :type attrs: list[str]
        :return: A dictionary representation of a Student instance.
        :rtype: dict
        """
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
    
    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with the values in the given JSON dictionary.
        :param json: A JSON dictionary representation of a Student instance.
        :type json: dict
        """
        for key, value in json.items():
            setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of a Student instance.
        :return: A string representation of a Student instance.
        :rtype: str
        """
        return "[Student] {} {} - {}".format(self.first_name, self.last_name, self.age)
