#!/usr/bin/python3
"""Defines unittests for state.py"""

import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    def setUp(self):
        """Set up any necessary test fixtures."""
        self.state = State()

    def tearDown(self):
        """Tear down any test fixtures that were set up."""
        del self.state

    def test_default_name(self):
        """Test that the default name attribute is an empty string."""
        self.assertEqual(self.state.name, "")

    def test_name_assignment(self):
        """Test assigning a name to the state."""
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")


if __name__ == '__main__':
    unittest.main()
