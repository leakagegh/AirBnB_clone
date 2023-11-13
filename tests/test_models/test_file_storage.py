#!/usr/bin/python3
"""Defines unittests or file_storage.py"""

import os
import unittest
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Tests for the FileStorage class"""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()
        self.storage.reload()

    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_all(self):
        """Test the 'all' method of FileStorage."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Test the 'new' method of FileStorage."""
        obj = BaseModel()
        self.storage.new(obj)
        all_objects = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), all_objects)

    def test_save_reload(self):
        """Test the 'save' and 'reload' methods of FileStorage."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Create a new storage instance to simulate a fresh start
        new_storage = FileStorage()
        new_storage.reload()

        all_objects = new_storage.all()
        self.assertIn("BaseModel.{}".format(obj1.id), all_objects)
        self.assertIn("BaseModel.{}".format(obj2.id), all_objects)


if __name__ == "__main__":
    unittest.main()
