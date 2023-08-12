#!/usr/bin/python3
"""
This file contain the base class.
"""


import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    class BaseModel that defines all common att/meth for other classes.
    """
    def __init__(self, *args, **kwargs):
        """
        the constructor of a BaseModel.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ["created_at", "updated_at"]:
                    f = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(value, f))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """
        return the string format of a instance.
        """
        return ("[{}] ({}) {}"
                "".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        updates the updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        """

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = str(datetime.isoformat(self.created_at))
        dictionary["updated_at"] = str(datetime.isoformat(self.updated_at))
        return dictionary
