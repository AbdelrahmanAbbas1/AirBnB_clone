#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class represents a command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """This command exits program"""
        return True

    def do_EOF(self, arg):
        """This command exits the program using EOF"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
