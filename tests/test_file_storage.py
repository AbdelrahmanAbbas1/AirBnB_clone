#!/usr/bin/python3
"""A unnitest for file_storage"""
import unittest
import os
from your_module_name import FileStorage  # Replace 'your_module_name' with the actual module name where your FileStorage class is defined

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # This method will be called before every test
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        # This method will be called after every test
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        storage = FileStorage()
        objects = storage.all()
        self.assertEqual(objects, FileStorage._FileStorage__objects)

    def test_new(self):
        storage = FileStorage()

        class TestObject:
            def __init__(self, _id):
                self.id = _id
                self.to_dict = lambda: {'id': _id}

        obj = TestObject("test_id")
        storage.new(obj)

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(FileStorage._FileStorage__objects[key], obj.to_dict())

    def test_save_and_reload(self):
        storage1 = FileStorage()
        storage2 = FileStorage()

        class TestObject:
            def __init__(self, _id):
                self.id = _id
                self.to_dict = lambda: {'id': _id}

        obj = TestObject("test_id")
        storage1.new(obj)
        storage1.save()
        storage2.reload()

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(FileStorage._FileStorage__objects[key], obj.to_dict())

if __name__ == '__main__':
    unittest.main()

