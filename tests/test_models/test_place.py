#!/usr/bin/python3
"""Defines unittests or place.py"""

import unittest
import os
from models.place import Place
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""
    def setUp(self):
        """Set up any necessary test fixtures."""
        self.place = Place()

    def tearDown(self):
        """Tear down any test fixtures that were set up."""
        del self.place

    def test_default_attributes(self):
        """Test that the default attributes have the expected values."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_assignment(self):
        """Test assigning values to the attributes."""
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Cozy Cabin"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 6
        self.place.price_by_night = 100
        self.place.latitude = 42.12345
        self.place.longitude = -71.67890
        self.place.amenity_ids = [1, 2, 3]

        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "456")
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 42.12345)
        self.assertEqual(self.place.longitude, -71.67890)
        self.assertEqual(self.place.amenity_ids, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
