#!/usr/bin/python3
from models.base_model import BaseModel


class State(BaseModel):
    """State class"""
    name = ""


def _init_(self, *args, **kwargs):
    """class constructor"""
    super()._init_(*args, **kwargs)
