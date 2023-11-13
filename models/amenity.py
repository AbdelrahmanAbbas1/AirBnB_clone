#!/usr/bin/python3
"""This module defines a Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class represents an amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of the class Amenity"""
        super().__init__(*args, **kwargs)
