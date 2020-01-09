class Network(object):
    """The model for a cable network."""

    def __init__(self, x, y, capacity):
        """Initializes the source location and capacity of the battery."""

        self.capacity = capacity
        self.source = (x, y)
        self.cables = list()

        sourceCable = (x, y)
        self.cables.append(sourceCable)

    def LoadNetwork(self, filePath):

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
                    networkData.append(float(element))

            # Appends to list
            newNetwork = Network(networkData[0], networkData[1], networkData[2])
            networks.append(newNetwork)

        return networks

    def __str__(self):
        return f"{self.capacity}, {self.source}, cables: {self.cables}"