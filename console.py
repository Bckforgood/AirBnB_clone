#!/usr/bin/python3
"""the HBnB console."""
import cmd
import json
import re
from models import storage
from shlex import split
from models.state import State
from models.base_model import BaseModel
import models.user
import models.state
import models.city
import models.amenity
import models.place
import models.review
from models.engine.file_storage import FileStorage


def parse(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    bracks = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if bracks is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:bracks.span()[0]])
            ret = [i.strip(",") for i in lexer]
            ret.append(bracks.group())
            return retl
    else:
        lexer = split(arg[:braces.span()[0]])
        ret = [i.strip(",") for i in lexer]
        ret.append(braces.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter class.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def do_EOF(self, line):
        """
        Exit the program at EOF
        """
        print("")
        return True
    
    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        al = parse(arg)
        if len(al) == 0:
            print("** class name missing **")
        elif al[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(al[0])().id)
            storage.save()
    
    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string rep of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of given id."""
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Shows string rep of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
