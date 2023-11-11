#!/usr/bin/python3
"""This module defines a BaseModel class"""
import uuid
from datetime import datetime


class BaseModel():
    """This class represents a basemodel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """Retrun string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the datetime"""
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Returns a dictionary with all keys/values of __dict__"""
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
