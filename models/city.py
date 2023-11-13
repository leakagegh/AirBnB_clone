#!/usr/bin/python3
""" Defines City(BaseModel) class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class represents a city and inherits from BaseModel."""
    state_id = ""
    name = ""
