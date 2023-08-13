#!/usr/bin/python3
"""the HBnB console."""
import cmd
import json
from models.state import State
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
