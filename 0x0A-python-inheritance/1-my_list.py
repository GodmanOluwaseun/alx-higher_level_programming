#!/usr/bin/python3

"""1-my_list
Class MyList that inherits from list.
"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Method that prints sorted listt of ints"""
        print (sorted(self))
