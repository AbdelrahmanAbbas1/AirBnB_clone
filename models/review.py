#!/usr/bin/python3
"""This module defines a Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class represents a review"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Instantiation of the class Review"""
        super().__init__(*args, **kwargs)
