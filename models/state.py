#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """State class"""
    name = ""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
