#!/usr/bin/python3

"""FileStorage module"""

import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_list = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class FileStorage():
    """Representation of a FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """class constructor"""
        pass

    def save(self):
        """serializes '__objects' to the JSON file"""
        dict = {}
        for key in self.__objects:
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict, f)

    def all(self):
        """returns the dictionary '__objects'"""
        return self.__objects

    def new(self, obj):
        """sets in '__objects' the 'obj' with key '<obj class name>.id'"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})

    def reload(self):
        """deserializes the JSON file to '__objects'
           (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.load(f)
            for i in dict:
                self.__objects[i] = class_list[dict[i]["__class__"]](**dict[i])
        except FileNotFoundError:
            pass
