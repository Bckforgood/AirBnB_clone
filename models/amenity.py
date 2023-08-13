#!/usr/bin/python3

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super()._init_(*args, **kwargs)
