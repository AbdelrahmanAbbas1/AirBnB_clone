#!/usr/bin/python3
"""This module defines a City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class represents a city"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of a the class city"""
        super().__init__(*args, **kwargs)
