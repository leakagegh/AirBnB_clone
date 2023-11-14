#!/usr/bin/python3
"""
HBNB Console Module

This module provides a command-line interface (CLI) for the HBNB project.
It allows users to interact with the application, create objects, retrieve
object information, update objects, and perform other actions.

"""

import cmd
from datetime import datetime
import re
import os
import sys
import uuid


from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from  models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNB Console Class

    This class implements the command-line interface (CLI)
    for the HBNB project.
    It inherits from the cmd.Cmd class provided by the cmd module.

    """

    # Determines the prompt for interactive/non-interactive modes
    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''

    # Dictionary mapping class names to their corresponding classes
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review
    }

    # List of dot commands supported by the console
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    # Dictionary mapping attribute names to their corresponding types
    types = {
        'number_rooms': int,
        'number_bathrooms': int,
        'max_guest': int,
        'price_by_night': int,
        'latitude': float,
        'longitude': float
    }

    def preloop(self):
        """
        Preloop Hook

        This method is executed before the command loop begins.
        It prints the prompt if the input stream
        is not connected to a terminal.

        """
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        """
        Precommand Hook

        This method is called just before the command is executed.
        It reformats the command line for advanced command syntax.

        Usage: <class name>.<command>([<id> [<*args> or <**kwargs>]])
        (Brackets denote optional fields in the usage example.)
        """
        _cmd = _cls = _id = _args = ''  # Initialize line elements

        # Scan for general formatting - i.e., '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:  # Parse line from left to right
            pline = line[:]  # Parsed line

            # Isolate <class name>
            _cls = pline[:pline.find('.')]

            # Isolate and validate <command>
            _cmd = pline[pline.find('.') + 1:pline.find('(')]
            if _cmd not in HBNBCommand.dot_cmds:
                raise Exception

            # If parentheses contain arguments, parse them
            pline = pline[pline.find('(') + 1:pline.find(')')]
            if pline:
                # Partition args: (<id>, [<delim>], [<*args>])
                pline = pline.partition(', ')  # pline converts to tuple

                # Isolate _id, stripping quotes
                _id = pline[0].replace('\"', '')

                # If arguments exist beyond _id
                pline = pline[2].strip()  # pline is now a string
                if pline:
                    # Check for *args or **kwargs
                    if pline[0] == '{' and pline[-1] == '}'\
                            and type(eval(pline)) is dict:
                        _args = pline
                    else:
                        _args = pline.replace(',', '')
            line = ' '.join([_cmd, _cls, _id, _args])

        except Exception as mess:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        """
        Postcommand Hook

        This method is called just after the command is executed.
        It prints the prompt if the input stream is not
        connected to a terminal.

        """
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        """
        Quit Command

        Exits the HBNB console.
        """
        exit(0)

    def help_quit(self):
        """
        Quit Command Help

        Prints the help documentation for the quit command.
        """
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        """
        EOF Command

        Handles the End-of-File (EOF) input to exit the program.
        """
        exit(0)

    def help_EOF(self):
        """
        EOF Command Help

        Prints the help documentation for the EOF command.
        """
        print("Exits the program without formatting\n")

    def emptyline(self):
        """
        Empty Line Override

        Overrides the emptyline method of the cmd.Cmd class.
        It prevents repeating the previous command when
        the user inputs an empty line.

        """
        return False

    def do_create(self, args):
        """
        Create Command

        Creates an instance of a class.
        The class name is provided as an argument.
        Additional attributes can be specified in the format:
        attributeName=attributeValue.

        """
        ignored_attrs = ('id', 'created_at', 'updated_at', '__class__')
        class_name = ''
        name_pattern = r'(?P<name>(?:[a-zA-Z]|_)(?:[a-zA-Z]|\d|_)*)'
        class_match = re.match(name_pattern, args)
        obj_kwargs = {}

        if class_match is not None:
            class_name = class_match.group('name')
            params_str = args[len(class_name):].strip()
            params = params_str.split(' ')
            str_pattern = r'(?P<t_str>"([^"]|\")*")'
            float_pattern = r'(?P<t_float>[-+]?\d+\.\d+)'
            int_pattern = r'(?P<t_int>[-+]?\d+)'
            param_pattern = '{}=({}|{}|{})'.format(
                name_pattern,
                str_pattern,
                float_pattern,
                int_pattern
            )

            for param in params:
                param_match = re.fullmatch(param_pattern, param)
                if param_match is not None:
                    key_name = param_match.group('name')
                    str_v = param_match.group('t_str')
                    float_v = param_match.group('t_float')
                    int_v = param_match.group('t_int')

                    if float_v is not None:
                        obj_kwargs[key_name] = float(float_v)
                    if int_v is not None:
                        obj_kwargs[key_name] = int(int_v)
                    if str_v is not None:
                        obj_kwargs[key_name] = str_v[1:-1].replace('_', ' ')
        else:
            class_name = args

        if not class_name:
            print("** class name missing **")
            return
        elif class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            if 'id' not in obj_kwargs:
                obj_kwargs['id'] = str(uuid.uuid4())
            if 'created_at' not in obj_kwargs:
                obj_kwargs['created_at'] = str(datetime.now())
            if 'updated_at' not in obj_kwargs:
                obj_kwargs['updated_at'] = str(datetime.now())

            new_instance = HBNBCommand.classes[class_name](**obj_kwargs)
            new_instance.save()
            print(new_instance.id)
        else:
            new_instance = HBNBCommand.classes[class_name]()
            for key, value in obj_kwargs.items():
                if key not in ignored_attrs:
                    setattr(new_instance, key, value)
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        """
        Provides help documentation for the create command.

        Usage: create <className> [attributeName=attributeValue ...]
        """
        print("Creates an instance of a class")
        print("You can optionally provide additional attributes with values")
        print("Exp: create User email=\"Omega@gmail.com\" password=\"Fh7!8\"")
        print()

    def do_show(self, args):
        """
        Shows information about an individual object.

        Usage: show <className> <objectId>
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # Guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """
        Provides help documentation for the show command.

        Usage: show <className> <objectId>
        """
        print("Shows information about an individual object")
        print("Example: show User 123")
        print()

    def do_destroy(self, args):
        """
        Destroys a specified object.

        Usage: destroy <className> <objectId>
        """

        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            storage.delete(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """
        Provides help documentation for the destroy command.

        Usage: destroy <className> <objectId>
        """
        print("Destroys a specified object")
        print("Example: destroy User 123")
        print()

    def do_all(self, args):
        """
        Shows all objects, or all objects of a class
        """
        print_list = []

        if args:
            args = args.split(' ')[0]  # Remove possible trailing args
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all().items():
                if k.split('.')[0] == args:
                    print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))

        print(print_list)

    def help_all(self):
        """
        Provides help documentation for the all command.

        Usage: all [className]
        """
        print("Shows all objects, or all objects of a class")
        print("Example: all User")
        print()

    def do_count(self, args):
        """
        Counts the number of instances of a class.

        Usage: count <className>
        """
        count = 0
        for k, v in storage.all().items():
            if args == k.split('.')[0]:
                count += 1
        print(count)

    def help_count(self):
        """
        Provides help documentation for the count command.

        Usage: count <className>
        """
        print("Counts the current number of class instances")
        print("Example: count User")
        print()

    def do_update(self, args):
        """
        Updates the attributes of a certain object.

        Usage: update <className> <id> <attributeName> <attributeValue>
        """
        c_name = c_id = att_name = att_val = kwargs = ''

        # Isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  # Class name not present
            print("** class name missing **")
            return
        if c_name not in HBNBCommand.classes:  # Class name invalid
            print("** class doesn't exist **")
            return

        # Isolate id from args
        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]
        else:  # Id not present
            print("** instance id missing **")
            return

        # Generate key from class and id
        key = c_name + "." + c_id

        # Determine if key is present
        if key not in storage.all():
            print("** no instance found **")
            return

        # First determine if kwargs or args
        if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
            kwargs = eval(args[2])
            args = []  # Reformat kwargs into list, ex: [<name>, <value>, ...]
            for k, v in kwargs.items():
                args.append(k)
                args.append(v)
        else:  # Isolate args
            args = args[2]
            if args and args[0] == '\"':  # Check for quoted arg
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')

            # If att_name was not a quoted arg
            if not att_name and args[0] != ' ':
                att_name = args[0]
            # Check for quoted val arg
            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            # If att_val was not a quoted arg
            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        # Retrieve dictionary of current objects
        new_dict = storage.all()[key]

        # Iterate through attr names and values
        for i, att_name in enumerate(args):
            # Block only runs on even iterations
            if (i % 2 == 0):
                att_val = args[i + 1]  # Following item is value
                if not att_name:  # Check for att_name
                    print("** attribute name missing **")
                    return
                if not att_val:  # Check for att_value
                    print("** value missing **")
                    return
                # Type cast as necessary
                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                # Update dictionary with name, value pair
                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()  # Save updates to file

    def help_update(self):
        """
        Provides help documentation for the update command.

        Usage: update <className> <id> <attributeName> <attributeValue>
        """
        print("Updates the attributes of a certain object")
        print("Example: update User 123 email \"new@example.com\"")
        print()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
