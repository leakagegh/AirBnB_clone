#!/usr/bin/python3
""" Defines unittesst for user.py"""

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUserModel(unittest.TestCase):
    """Tests for the User class"""

    def setUp(self):
        self.user = User()

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_user_inherits_from_base_model(self):
        """Test if User inherits from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))

    def test_user_attributes(self):
        """Test if User has the expected attributes"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_default_attribute_values(self):
        """Test if default attribute values are correctly initialized."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
