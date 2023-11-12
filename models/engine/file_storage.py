#!/usr/bin/python3
"""This module defines a FileStorage class"""
import json
import os


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """This function serializes __objects to JSON"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """This function deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    FileStorage.__objects = json.load(f)
            except FileNotFoundError:
                return
