#!/usr/bin/python3
from models.base_model import BaseModel

class User(BaseModel):
    """
    User class inherits from BaseModel.
    """

    def _init_(self, *args, **kwargs):
        """
        Initialize User instance.
        """
        super()._init_(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def _str_(self):
        """
        Return the string representation of User.
        """
        return "[User] ({}) {}".format(self.id, self._dict_)

    def _init_(self, *args, **kwargs):
        """class constructor"""
        super()._init_(*args, **kwargs)
