#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
	 __file_path = "file.json"
	__objects = {}

	def all(self):
		return FileStorage.__objects

	def new(self, obj):
		key = "{}.{}".format(obj.__class__.____name__, obj.id)
		FileStorage.__objects[key] = obj

	def save(self):
		serialized_objects = {}
		for key, obj in FileStorage.__objects.items():
			serialized_objects[key] = obj.to_dict()
			with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
				json.dump(serialized_objects, file)

	def reload(self):
		try:
			with open(FileStorage.__file_path, 'r', encoding="utf-8") as file:
				data = json.load(file)
				for key, value in data.items():
					class_name, obj_id = key.split('.')
					obj_class = eval(class_name)
					obj = obj_class(**value)
					FileStorage.__objects[key] = obj
		except FileNotFoundError:
			pass
