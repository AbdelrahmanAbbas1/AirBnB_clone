#!/usr/bin/python3
"""This module defines unittests for BaseModel"""
import unittest
from models.base_model import BaseModel


class TestBaseModel_instantiaion(unittest.TestCase):
    """This class represents unittest cases for testing of instantiation"""

    def test_base_model_no_ag(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1, b2, "Have same id")


if __name__ == "__main__":
    unittest.main()
