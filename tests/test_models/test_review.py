#!/usr/bin/python3
"""Defines unittests or review.py"""

import unittest
import os
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Tests for the Review class"""

    def setUp(self):
        """Set up any necessary test fixtures."""
        self.review = Review()

    def tearDown(self):
        """Tear down any test fixtures that were set up."""
        del self.review

    def test_default_attributes(self):
        """Test that the default attributes have the expected values."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_assignment(self):
        """Test assigning values to the attributes."""
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Great place to stay!"

        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Great place to stay!")


if __name__ == '__main__':
    unittest.main()
