#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""
    def _init_(self, *args, **kwargs):
        """class constructor"""
        super()._init_(*args, **kwargs)
