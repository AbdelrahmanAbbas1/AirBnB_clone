#!/usr/bin/python3
"""This module defines a FileStorage class"""
import json
import os
from models.base_model import BaseModel


class FileStorage():
    """This class represents a filestorage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """This function instantiate an instance of the class"""

    def all(self):
        """This fucntion returns __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """This function sets the obj in __objects"""
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """This function serializes __objects to JSON"""
        o_dict = FileStorage.__objects
        obj_dict = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """This function deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    for obj in obj_dict.values():
                        cls_name = obj.pop("__class__", None)
                        if cls_name == "BaseModel":
                            self.new(BaseModel(**obj))
            except FileNotFoundError:
                return
