class Network(object):
    """The model for a cable network."""

    def __init__(self, x, y, capacity):
        """Initializes the source location and capacity of the battery."""

        self.capacity = capacity
        self.source = (x, y)
        self.cables = list()

        sourceCable = (x, y)
        self.cables.append(sourceCable)

    def __str__(self):
        return f"{self.capacity}, {self.source}, cables: {self.cables}"