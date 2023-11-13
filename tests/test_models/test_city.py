#!/usr/bin/python3
"""Defines unittest for city.py"""

import unittest
import os
from models.city import City
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """ Tests for the City class"""

    def setUp(self):
        """Set up any necessary test fixtures."""
        self.city = City()

    def tearDown(self):
        """Tear down any test fixtures that were set up."""
        del self.city

    def test_default_state_id(self):
        """Test that the default state_id attribute is an empty string."""
        self.assertEqual(self.city.state_id, "")

    def test_default_name(self):
        """Test that the default name attribute is an empty string."""
        self.assertEqual(self.city.name, "")

    def test_state_id_assignment(self):
        """Test assigning a state_id to the city."""
        self.city.state_id = "CA"
        self.assertEqual(self.city.state_id, "CA")

    def test_name_assignment(self):
        """Test assigning a name to the city."""
        self.city.name = "Los Angeles"
        self.assertEqual(self.city.name, "Los Angeles")


if __name__ == '__main__':
    unittest.main()
