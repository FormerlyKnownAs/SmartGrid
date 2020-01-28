"""

network.py

Houses the Network class, also loads batteries from a given input files
and generates network objects.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""


import csv

class Network(object):
    """The model for a cable network."""

    def __init__(self, x, y, capacity):
        """Initializes the source location and capacity of the battery."""

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

def LoadNetwork(filePath):
    """ Reads out, parses input file, generates
        network objects. """

    # Makes list to return to be filled with csv data
    networks = []

    with open(filePath, "r") as f:

        # Skips header
        csvreader = csv.reader(f)
        next (csvreader, None)

        # Reads the lines
        for line in f:

            networkData = []

            for element in line.split(","):

                # Reads out numbers and stores them as floats
                element = element.strip('"[]"')
                networkData.append(element)

            # Appends to list
            newNetwork = Network(int(networkData[0]), int(networkData[1]), 
                                    float(networkData[2]))
            networks.append(newNetwork)

    return networks