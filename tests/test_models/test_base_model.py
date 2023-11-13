#!/usr/bin/python3
"""Defines unittests for base_model.py"""

import models
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def test_create_base_model_with_no_arguments(self):
        """Test creating a BaseModel instance with no arguments."""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_create_base_model_with_attributes(self):
        """Test creating a BaseModel instance with attributes."""
        data = {
            'name': 'Test Model',
            'value': 42
        }
        model = BaseModel(**data)
        self.assertEqual(model.name, 'Test Model')
        self.assertEqual(model.value, 42)

    def test_create_base_model_with_invalid_attributes(self):
        """Test creating a BaseModel instance with invalid attributes."""
        data = {
            'created_at': '2022-01-01T00:00:00.000',
            'updated_at': '2022-01-02T00:00:00.000'
        }
        model = BaseModel(**data)
        # created_at and updated_at should not be directly set using kwargs
        self.assertNotEqual(model.created_at, '2022-01-01T00:00:00.000')
        self.assertNotEqual(model.updated_at, '2022-01-02T00:00:00.000')

    def test_save_method_updates_updated_at(self):
        """Test that the save method updates the 'updated_at' attribute."""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method for creating a dictionary representation."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)


if __name__ == '__main__':
    unittest.main()
