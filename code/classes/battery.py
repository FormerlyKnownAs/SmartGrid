import csv

class Battery(object):
    """Het model voor de batterij."""

    def __init__(self, x, y, capacity):
        """Initializeert de batterij."""

        self.coordinates = (x, y)
        self.capacity = capacity

    def __str__(self):
        return f"Battery: {self.coordinates}"

def LoadBatteries(filePath):

    # Makes list to return to be filled with csv data
    batteries = []

    with open(filePath, "r") as f:

        # Skips header
        csvreader = csv.reader(f)
        next(csvreader, None)

        # Reads the lines
        for line in f:

            batteryData = []

            for element in line.split(","):

                # Reads out numbers and stores them as floats
                element = element.strip('"[]"')
                batteryData.append(float(element))

            # Appends to list
            newBattery = Battery(batteryData[0], batteryData[1], batteryData[2])
            batteries.append(newBattery)

    return batteries