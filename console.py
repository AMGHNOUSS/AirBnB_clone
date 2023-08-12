#!/usr/bin/python3
""" Entry point of the command interpreter """
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Command"""
    
    l_c = ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'State', 'Review']
    prompt = "(hbnb) "
    
    def emptyline(self):
        """do nothing when empty line"""
        pass

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def do_EOF(self, line):
        """ EOF command to exit the command interpreter """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()