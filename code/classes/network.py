"""

network.py

Houses the Network class, also loads batteries from a given input files
and generates network objects.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""


import csv

class Network(object):
    """ The model for a cable network. """

    def __init__(self, x, y, capacity):
        """ Initializes the source location 
            and capacity of the battery. """

        self.source = (x, y)
        self.capacity = capacity
        self.startcapacity = capacity
        self.houses = []
        self.houses2 = set()
        self.cables = set()

        sourceCable = (x, y)
        self.cables.add(sourceCable)

    def __str__(self):
        return f"{self.capacity}, {self.source}, cables: {self.cables}"