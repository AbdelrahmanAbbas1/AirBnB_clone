#!/usr/bin/python3
"""This module defines State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class represents a state"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of the State"""
        super().__init__(*args, **kwargs)
