#!/usr/bin/env python3
"""entry to the program"""

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class to impliment the cmd module"""
    prompt = "(hbnb) "

    valid_classes = [
            "Amenity", "BaseModel", "City",
            "Place", "Review", "State", "User"
            ]

    def do_all(self, arg):
        """Prints all string representations"""
        all_instances = storage.all()
        if not arg:
            for instance in all_instances.values():
                print(instance)
        else:
            class_name = arg.strip()
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return
            else:
                filtered_instances = {
                        k: v for k, v in all_instances.items()
                        if k.startswith(class_name + ".")
                        }
                for instance in filtered_instances.values():
                    print(instance)

    def do_create(self, arg):
        """Creates a new instance and prints the ID."""
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.strip()
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_update(self, arg):
        """Updates an instance based on the class name"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instance_id = args[1]

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]
        if attribute_name in ['id', 'created_at', 'updated_at']:
            print("** cannot update id, created_at, or updated_at **")
            return

        instance = objects[key]
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instance_id = args[1]

        objects = storage.all()
        key = "{}.{}".format(class_name, instance_id)
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = storage.all()
        if key in all_instances:
            print(all_instances[key])
        else:
            print("** no instance found **")

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def emptyline(self):
        """prevents command repetition"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
