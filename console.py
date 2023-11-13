#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
import json

classes = {"BaseModel": BaseModel}


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
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """show command to show the insatnce of a class"""
        args = arg.split()
        obj_list = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return False
        else:
            if args[0] in classes:
                if len(args) > 1:
                    key = f"{args[0]}.{args[1]}"
                    if key in obj_list:
                        print(obj_list[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """destroy command to delete in instance from the list"""
        args = arg.split()
        obj_list = storage.all()
        if len(args) > 0:
            if args[0] in classes:
                if len(args) > 1:
                    key = f"{args[0]}.{args[1]}"
                    if key in obj_list:
                        del obj_list[key]
                        storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """all command to print all string representation of all instances"""
        obj_list = storage.all()
        list_rep = []
        if len(arg) == 0:
            for obj in obj_list.values():
                list_rep.append(str(obj))
            print("[", end="")
            print(", ".join(list_rep), end="")
            print("]")
        elif arg in classes:
            for obj in obj_list.values():
                if arg == obj.__class__.__name__:
                    list_rep.append(str(obj))
            print("[", end="")
            print(", ".join(list_rep), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update command to update the instance"""
        args = arg.split()
        obj_list = storage.all()
        if len(args) != 0:
            if args[0] in classes:
                if len(args) > 1:
                    key = f"{args[0]}.{args[1]}"
                    if key in obj_list:
                        if len(args) > 2:
                            if len(args) > 3:
                                obj = obj_list[key]
                                setattr(obj_list[key], args[2], args[3])
                                obj_list[key].save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
