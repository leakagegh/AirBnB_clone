#!/usr/bin/python3
"""Defines unittests or amenity.py"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""

    def setUp(self):
        """Set up any necessary test fixtures."""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down any test fixtures that were set up."""
        del self.amenity

    def test_default_name(self):
        """Test that the default name attribute is an empty string."""
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        """Test assigning a name to the amenity."""
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")


if __name__ == '__main__':
    unittest.main()
