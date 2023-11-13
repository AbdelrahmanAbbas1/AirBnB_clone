#!/usr/bin/python3
"""This module defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class represents a user"""
    email = ""
    password = ""
    firs_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Instantiate user"""
        super().__init__(*args, **kwargs)
