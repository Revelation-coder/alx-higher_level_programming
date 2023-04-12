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
