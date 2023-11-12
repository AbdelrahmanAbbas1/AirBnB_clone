#!/usr/bin/python3

""" Defines the Class BaseModel"""
import sys
import models
from uuid import uuid4
from datetime import datetime
from models import storage

class BaseModel():
	""" Represents the base model of a HBnB project."""
	def __init__(self, *args, **kwargs):
		tform = "%Y-%m-%dT%H:%M:%S.%f"
        
        # If kwargs is not empty, populate attributes from the dictionary representation
		if kwargs:
			for key, value in kwargs.items():
				if key == "created_at" or key == "updated_at":
					# Convert string to datetime
					setattr(self, key, datetime.strptime(value, tform))
				else:
					setattr(self, key, value)
		else:
			# Create a new instance with a new id and current created_at and updated_at
			self.id = str(uuid4())
			self.created_at = datetime.now()
			self.updated_at = datetime.now()
			storage.new(self)

	def save(self):
	"""updates the updated_at to the current time"""
		self.updated_at = datetime_now()
		models.storage.save()

	def to_dict(self):
	""" creates a dictionary representation of the object"""
		my_dict = self.__dict__.copy()
		my_dict["created_at"] = self.created_at.isoformat(
		my_dict["updated_at"] = self.updated_at.isoformat()
		my_dict["__class__"] = self.__class__.__name__
		return my_dict
	
	def __str__(self):
	""" Returns the printed str of the BaseModel instances"""
		clsname = self.__class__.__name__
		return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
