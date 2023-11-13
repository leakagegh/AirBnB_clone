#!/usr/bin/python3
"""Defines a Review(BaseModel) class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class represents a review and inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""
