#!/usr/bin/python3
""" Defines a Amenity(BaseModel) class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class represents an amenity and inherits from BaseModel."""
    name = ""
