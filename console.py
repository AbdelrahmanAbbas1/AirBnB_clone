#!/usr/bin/python3
"""A console program that contains an entry point of a command intep"""
import cmd

class HBNBCommand(cmd.Cmd):
	""" Defines the HBnB program
	Att:
		prompt (str): command prompt
	"""
	prompt "(hbnb)"

	def emptyline(self):
		"""Do nothing upon receiving an empty line."""
		pass

	def default(self, arg):
		"""Default behavior for cmd module when input is invalid"""
		argdict = {
			"all": self.do_all,
			"show": self.do_show,
			"destroy": self.do_destroy,
			"count": self.do_count,
			"update": self.do_update
		}
		match = re.search(r"\.", arg)
		if match is not None:
			argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
			match = re.search(r"\((.*?)\)", argl[1])
			if match is not None:
			command = [argl[1][:match.span()[0]], match.group()[1:-1]]
				if command[0] in argdict.keys():
				call = "{} {}".format(argl[0], command[1])
				return argdict[command[0]](call
		print("*** Unknown syntax: {}".format(arg))
		return False

	def do_quit(self, arg):
		"""quit command to exit the program"""
		return true

	def do_EoF(self, arg):
		"""an action to end a file"""
		print ("") #Print a newline for better formatting
	 	return true

	def do_create(self, arg):
		"""create a class instance then print an id"""
		argl = parse(arg)
		if len(arg) == 0:
			print("** class name missing **")
		elif argl[0] not in HBNBCommand.__classes:
			print("** class doesn't exist **")
		else:
			print(eval(argl[0])().id)
			storage.save()
	
	def do_count(self, arg):
		"""Usage: count <class> or <class>.count()"""
		argl = parse(arg)
		count == 0
		for obj in storage.all().values():
			if argl[0] == obj.__class__.__name__:
				count += 1
		print(count)

	def do_show(self, arg):
		"""Prints the string representation of an instance"""
		argl = parse(arg)
		objdict storage.all()
		if len(argl) == 0:
			print("** class name missing **")
		elif argl[0] not in HBNBCommand.__classes:
			print("** class doesn't exist **")
		elif len(argl) == 1:
			print("** instance id missing **")
		elif "{}.{}".format(argl[0], argl[1]) not in objdict:
			print("** no instance found **")
		else:
			print(objdict["{}.{}".format(argl[0], argl[1])]))

	def do_destroy(self, arg):
		"""Deletes an instance based on the class name and id"""
		argl = parse(arg)
		objdict = storage.all()
		if len(argl) == 0:
			print("** class name missing **")
		elif argl[0] not in HBNBCommand.__classes:
			print("** class doesn't exist **")
		elif len(argl) == 1:
			print("** instance id missing **")
		elif {}.{}.format(argl[0], argl[1]) not in objdict.keys():
			print("** no instance found **")
		else:
			del objdict["{}.{}".format(argl[0], argl[1])]
			storage.save()

	def do_all(self, arg):
		"""Prints all string representations of all instances"""
		argl = parse(arg)
		if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
			print("** class doesn't exist **")
		else:
			obj_list = []
			for obj in storage.all().values():
				if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
					obj_list.append(obj.__str__())
				elif len(argl) == 0:
					obj_list.append(obj.__str__())
			print(obj_list)

	def do_update(self, arg):
		"""Updates an instance based on the class name and id"""
		argl = parse(arg)
		objdict = storage.all()
		if len(argl) == 0:
			print("** class name missing **")
			return False
		if argl[0] not in HBNBCommand.__classes:
			print("** class doesn't exist **")
			return False
		if len(argl) == 1:
			print("** instance id missing **")
			return False
		if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
			print("** no instance found **")
			return False
		if len(argl) == 2:
			print("** attribute name missing **")
			return False
		if len(argl) == 3:
			try:
				type(eval(argl[2])) != dict
			except NameError:
				print("** value missing **")
				return False
		if len(argl) == 4:
			obj = objdict["{}.{}".format(argl[0], argl[1])]
			if argl[2] in obj.__class__.__dict__.keys():
				valtype = type(obj.__class__.__dict__[argl[2]])
				obj.__dict__[argl[2]] = valtype(argl[3])
			else:
				obj.__dict__[argl[2]] = argl[3]
			elif type(eval(argl[2])) == dict:
				obj = objdict["{}.{}".format(argl[0], argl[1])]
				for i, n in eval(argl[2]).items():
					if (i in obj.__class__.__dict__.keys() and
						type(obj.__class__.__dict__[i]) in {str, int, float}):
					valtype = type(obj.__class__.__dict__[i])
					obj.__dict__[i] = valtype(n)
				else:
					obj.__dict__[i] = n
			storage.save()
		


if __name__ == "__main__":
	HBNBCommand().cmdloop()
