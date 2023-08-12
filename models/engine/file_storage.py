#!usr/bin/python3
"""
Contain class FileStorage.
"""
import json
import os


class FileStorage:
    """
    FileStorage class that serializes instances to a JSON
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """

        cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cls_name, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        dictonary = {}

        for key, value in FileStorage.__objects.items():
            dictonary[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(json.dumps(dictonary))

    def reload(self):
        """
        deserializes the JSON file to __objects
        """

        from models.base_model import BaseModel
        dct = {"BaseModel": BaseModel}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                file_str = json_file.read()
                dictonary = json.loads(file_str)
                for value in dictonary.values():
                    self.new(dct[value['__class__']](**value))
