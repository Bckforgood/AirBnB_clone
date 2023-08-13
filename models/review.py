#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class"""
    place_id = ""
    user_id = ""
    text = ""

    def _init_(self, *args, **kwargs):
        """class constructor"""
        super()._init_(*args, **kwargs)
