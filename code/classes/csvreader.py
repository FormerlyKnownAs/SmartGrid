import csv
from code.classes.house import House
from code.classes.network import Network

def LoadHouses(filePath):
    """ Reads out, parses input file, generates
        House objects. Takes a filepath as an argument. """

    # Makes list to return to be filled with csv data
    houses = []

    with open(filePath, "r") as f:

        # Skips header
        csvreader = csv.reader(f)
        next (csvreader, None)

        # Reads the lines
        for line in f:

            houseData = []

            for element in line.split(","):

                # Reads out numbers
                houseData.append(element)

            # Appends to list
            newHouse = House(int(houseData[0]), int(houseData[1]), float(houseData[2]))
            houses.append(newHouse)

    return houses

def LoadNetwork(filePath):
    """ Reads out, parses input file, generates
        network objects. Takes a filepath as an
        argument. """

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
