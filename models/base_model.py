#!/usr/bin/python3
"""This module defines a BaseModel class"""
import uuid
from datetime import datetime


class BaseModel():
    """This class represents a basemodel"""
    def __init__(self):
        """Instantiation of the class and assigning values to its attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Retrun string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary with all keys/values of __dict__"""
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
