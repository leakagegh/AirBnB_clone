#!/usr/bin/python3
""" Defines User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a User class with attributes for email, password,
    first_name and last name.
    """
    def __init__(self, email="", password="", first_name="", last_name=""):
        """Initializes user object"""

        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        """Return a string representation of the User object."""

        return "User(email='{}', password='{}', first_name='{}',\
                last_name='{}')".format(self.email, self.password,
                                        self.first_name, self.last_name)
