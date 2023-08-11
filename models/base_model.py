#!/usr/bin/python3
"""
This file contain the base class.
"""

import uuid, datetime
class BaseModel:
    """
    class BaseModel that defines all common att/meth for other classes.
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        return "[<BaseModel>] ({}) <{}>".format(self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = str(datetime.datetime.isoformat(self.created_at))
        dictionary["updated_at"] = str(datetime.datetime.isoformat(self.updated_at))
        return dictionary