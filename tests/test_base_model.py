#!/usr/bin/python3
"""A unnitest for base_model"""
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_str_representation(self):
        model = BaseModel()
        string_representation = str(model)
        self.assertIn('BaseModel', string_representation)
        self.assertIn(model.id, string_representation)

    def test_save_method(self):
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model.id, model_dict['id'])
        self.assertEqual(model.created_at.isoformat(), model_dict['created_at'])
        self.assertEqual(model.updated_at.isoformat(), model_dict['updated_at'])
        self.assertEqual('BaseModel', model_dict['__class__'])
    
    def test_id_uniqueness(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at_and_updated_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()

