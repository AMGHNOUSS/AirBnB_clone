#!/usr/bin/python3
"""
This file contain BaseModal tests
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    clas to test all cases
    """

    def setUp(self):
        self.model = BaseModel()
        self.model.name = "Brahim"
        self.model.number = 89

    def tearDown(self):
        pass

    def test_BaseModel(self):
        """ Test attributest values of BaseModel instance """

        model_json = self.model.to_dict()

        self.assertEqual(self.model.name, "Brahim")
        self.assertEqual(self.model.number, 89)
        self.assertEqual("BaseModel", model_json["__class__"])
        self.assertEqual(self.model.id, model_json["id"])
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save(self):
        """ chacks if save method updates the public instances """

        self.model.save()

        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict(self):
        """ chacks if ro_dict  method work """

        dirct = self.model.to_dict()

        self.assertIsInstance(dirct, dict)
        self.assertIsInstance(dirct["created_at"], str)
        self.assertIsInstance(dirct["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
