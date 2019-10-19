"""
miniabm is a minimalist agent based modeling tool for python.
This package allows the user to easily create objects with prespecified attributes, group the objects according the their attributes and change them in a batch.
"""

import random


class agent:
    """
    This class has one predefined attribute: id. The id attribute is an identification number generated for each newly created object of this class.
    """
    def __init__(self):
        global count
        count += 1
        self.id = count


class agents:
    """
    An object of this class has two predefined attributes: olist and selection. Both are initialized as empty lists.
    olist is a list containing all objects created under the class agent with method crt.
    selection consists of a the last object selection made (with methods returning self).
    All methods returning self will change the current selection list and
    can be used in dot notation following any other method returning the same thing.
    """
    def __init__(self):
        global count
        count = 0
        self.alist = []
        self.selection = []

    def __call__(self):
        self.selection = self.alist
        return self

    def who(self, arg):
        """
        Takes the current object selection and selects objects by their id

        :param args:
            List of integer number

        :return:
            self
        """
        self.selection = [x for i in arg for x in self.alist if x.id == i]
        return self

    def crt(self, arg, **kwargs):
        """
        Create new agent objects and set their attributes

        :param arg:
            the number of new objects

        :param kwargs:
            attributes and corresponding values or functions

        :return:
            self
        """
        self.selection = [agent() for _ in range(int(arg))]
        if len(kwargs) != 0:
            self.set(1, **kwargs)
        self.alist += self.selection
        return self

    def set(self, repeat=1, **kwargs):
        """
        Set or change attributes of objects under selection

        :param repeat:
            integer number indicating the number of repetitions (DEFAULT=1)
        :param kwargs:
            attributes and corresponding values or functions
        :return:
            self
        """
        kwargs.pop('id', None)
        for i in range(repeat):
            for (attr, func) in kwargs.items():
                if callable(func):
                    [setattr(x, attr, func(getattr(x, attr, func))) for x in self.selection]
                else:
                    [setattr(x, attr, func) for x in self.selection]
        return self

    def w(self, **kwargs):
        """
        Select objects conditionally from the current object selection

        :param kwargs:
            attributes and corresponding values or functions
        :return:
            self
        """
        for (attr, func) in kwargs.items():
            if callable(func):
                self.selection = [x for x in self.selection if func(getattr(x, attr))]
            else:
                self.selection = [x for x in self.selection if getattr(x, attr) == func]
        return self

    def w_max(self, *args):
        """
        Select all objects with the maximum value of the specified attribute. More than one attribute can be specified

        :param args:
            a string specifying an attribute
        :return:
            self
        """
        for attr in args:
            maxval = max(self.tell(attr))
            self.selection = [x for x in self.selection if getattr(x, attr) == maxval]
        return self

    def w_min(self, *args):
        """
        Select all objects with the minimum value of the specified attribute. More than one attribute can be specified

        :param args:
            strings specifying attributes
        :return:
            self
        """
        for attr in args:
            minval = min(self.tell(attr))
            self.selection = [x for x in self.selection if getattr(x, attr) == minval]
        return self

    def other(self):
        """
        Select all objects other than the current selection

        :return:
            self
        """
        self.selection = [x for x in self.alist if x not in self.selection]
        return self

    def remove(self):
        """
        Remove all objects under selection

        :return:
            self
        """
        self.alist = [x for x in self.alist if x not in self.selection]
        self.selection = []
        return self

    def clone(self, arg):
        """
        Clone objects under selection

        :param arg:
            number of clones
        :return:
            self
        """
        for x in self.selection:
            args = vars(x)
            self.crt(arg, **args)
        return self

    def n_of(self, arg):
        """
        Sample a specified number of objects under selection

        :param arg:
            number of samples
        :return:
            self
        """
        self.selection = random.sample(self.selection, arg)
        return self

    def tell(self, arg):
        """
        List all values of a specified attribute for the current object selection

        :param arg:
            a string specifying an attribute
        :return:
            List of attribute values
        """
        return [getattr(x, arg) for x in self.selection]

    def ids(self):
        """
        List all id numbers of the current object selection

        :return:
            List of integers
        """
        return self.tell('id')

    def show(self):
        """
        Print object's dictionaries
        """
        for x in self.selection:
            print(vars(x))

    def slist(self):
        """
        List objects under selection

        :return:
            List of objects
        """
        return self.selection
