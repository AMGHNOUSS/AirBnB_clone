#!/usr/bin/python3
"""
Defines amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Define amenitie that user can choose from to offer at its place"""
    name = ""