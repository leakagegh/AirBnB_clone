#!/usr/bin/python3
""" Defines the BaseModel class"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class defining common attributes and methods.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of base model.
        *args: variable-length argument list.
        ***kwargs: keyword arguments.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime
                            (value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
            self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            models.storage.new(self)

    def save(self):
        """
        Updates the 'updated_at' attribute with current date time
        and saves to the JSON file.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of the object.
        """
        class_name = self.__class__.__name__
        data = self.__dict__.copy()
        data['__class__'] = class_name
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()

        return data

    @classmethod
    def from_dict(cls, data):
        """
        Recreates a BaseModel instance from a dictionary representation.
        """
        if '__class__' in data:
            class_name = data['__class__']
            if class_name == cls.__name__:
                if 'created_at' in data:
                    data['created_at'] = data['created_at']

                if 'updated_at' in data:
                    data['updated_at'] = data['updated_at']

                return cls(**data)
        return None

    def __str__(self):
        """
        Returns a string representation of the object.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def __iter__(self):
        self.attribute_values = list(self.__dict__.values())
        self._index = 0
        return self

    def __next__(self):
        if not hasattr(self, '_index'):
            raise StopIteration

        if self._index < len(self.attribute_values):
            result = self.attribute_values[self._index]
            self._index += 1

            # Check if the attribute is a datetime object and format it
            if isinstance(result, datetime):
                result = result.isoformat()

            return result
        else:
            raise StopIteration
