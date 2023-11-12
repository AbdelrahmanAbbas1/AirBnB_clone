#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """This class represents a command interpreter"""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing if it's an emptyline"""
        pass

    def do_create(self, arg):
        """create command to create an instance of class"""
        if len(arg) != 0:
            if arg == "BaseModel":
                obj = BaseModel()
                obj.save()
            else:
                print("class doesn't exist")
        else:
            print("class name missing")

    def do_show(self, arg):
        """show command to show the insatnce of a class"""
        args = arg.split()
        if len(args) > 0:
            obj_dict = storage.all()
            for o in obj_dict.values():
                if args[0] == o["__class__"] and args[1] == o["id"]:
                    print(o)

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
