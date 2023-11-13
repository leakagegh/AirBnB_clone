#!/usr/bin/python3
"""Defines unittests for console.py"""

import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Tests testing console.py"""

    def setUp(self):
        """setup the unnitests"""
        self.hbnb_command = HBNBCommand()

    def test_create(self):
        """test cases for create method"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("**"))
            self.assertIn("created", output)

    def test_show(self):
        """test cases for show"""
        base_model_instance = BaseModel()
        self.hbnb_command.my_instances["test_instance"] = base_model_instance

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("show BaseModel test_instance")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("BaseModel"))
            self.assertIn(str(base_model_instance), output)

    def test_destroy(self):
        """test cases for destroy method"""
        base_model_instance = BaseModel()
        self.hbnb_command.my_instances["test_instance"] = base_model_instance

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("destroy BaseModel test_instance")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("Instance deleted"))

    def test_all(self):
        """test cases for all"""
        base_model_instance = BaseModel()
        self.hbnb_command.my_instances["test_instance"] = base_model_instance

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(base_model_instance), output)

    def test_update(self):
        """test cases for update"""
        base_model_instance = BaseModel()
        self.hbnb_command.my_instances["test_instance"] = base_model_instance

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            self.hbnb_command.onecmd("update BaseModel\
                    test_instance name John")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.startswith("**"))
            self.assertIn("updated", output)
            self.assertEqual(base_model_instance.name, "John")


if __name__ == '__main__':
    unittest.main()
