#!usr/bin/python3
"""
This file contain all test cases for file_storage.
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test FileStorage class"""

    def setUp(self):
        """The setUp func"""
        self.model = BaseModel()
        self.model.name = "Brahim"

    def test_FileStorage(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testStoreBaseModel(self):
        """ Test save and reload functions """
        self.model.save()

        dictonary = self.model.to_dict()
        all_obj = storage.all()

        key = dictonary["__class__"] + "." + dictonary["id"]
        self.assertEqual(key in all_obj, True)
        self.assertEqual(dictonary['name'], "Brahim")

        created = dictonary["created_at"]
        updated = dictonary["updated_at"]

        self.model.name = "bousskry"
        self.model.save()
        dictonary = self.model.to_dict()
        all_obj = storage.all()

        self.assertEqual(key in all_obj, True)

        self.assertEqual(created, dictonary["created_at"])
        self.assertNotEqual(updated, dictonary["updated_at"])
        self.assertEqual(dictonary["name"], "bousskry")

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)

    def testsave(self):
        """verify if JSON exists"""
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testreload(self):
        """test if reload """
        self.model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        obj = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(obj, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(obj[key].to_dict(), value.to_dict())

    def testSaveSelf(self):
        """ Check save self """
        msg = "FileStorage.save() takes 1 positional argument but 2 were given"
        with self.assertRaises(TypeError) as e:
            FileStorage.save(self, 100)

        self.assertEqual(str(e.exception), msg)

    def test_save_FileStorage(self):
        """ Test if 'new' method is working good """
        var1 = self.model.to_dict()
        new_key = var1['__class__'] + "." + var1['id']
        storage.save()
        with open("file.json", 'r') as fd:
            var2 = json.load(fd)
        new = var2[new_key]
        for key in new:
            self.assertEqual(var1[key], new[key])


if __name__ == '__main__':
    unittest.main()
