#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel

class City(BaseModel):
	"""Represents the class city
	Att:
		state_id (str): the state id
		name (str) : name of the city
	"""
	state_id =  ""
	name = ""
	
