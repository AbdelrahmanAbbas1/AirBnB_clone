#!/usr/bin/python3
"""This module defines a BaseModel class"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """This class represents a basemodel"""
    def __init__(self, *args, **kwargs):
        """Instantiation of the class and assigning values to its attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k == "__class__":
                    continue
                self.__dict__[k] = v
        else:
            storage.new(self)

    def __str__(self):
        """Retrun string representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary with all keys/values of __dict__"""
        full_dict = self.__dict__.copy()
        full_dict["created_at"] = self.created_at.isoformat()
        full_dict["updated_at"] = self.updated_at.isoformat()
        full_dict["__class__"] = self.__class__.__name__
        return full_dict
