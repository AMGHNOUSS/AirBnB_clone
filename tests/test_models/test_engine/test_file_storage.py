#!usr/bin/python3
"""
This file contain all test cases for file_storage.
"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage


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