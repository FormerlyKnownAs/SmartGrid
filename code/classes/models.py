"""
06-01-2020


De modellen voor de SmartGrid assignment.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

class House(object):
    """Het model voor het huis object."""
    
    def __init__(self, x, y, output):
        """Initializeert het huis."""

        self.coordinates = (x, y)
        self.output = output
        self.route = (None, None)
        self.battery = (None, None)
        self.cost = 0

    def BatteryCheck(self, batteries):
        """Checks the best battery based on distance and current capacity."""

        # Makes empty list to store distance between house and battery
        distanceList = []


        for battery in batteries:

            # Checks capacity and if available checks distance to battery
            if battery.capacity > self.output:
                distance = abs(self.coordinates[0] - battery.coordinates[0]) + abs(self.coordinates[1] - battery.coordinates[1])
                print(f"Self = {self.coordinates}. Battery = {battery.coordinates}, Capacity = {battery.capacity}")

                distanceList.append(distance)
            else:
                distanceList.append(None)

        # Finds nearest available battery
        shortestDistance = min(i for i in distanceList if i is not None)
        shortestIndex = distanceList.index(shortestDistance)

        # Sets battery and route
        self.battery = batteries[shortestIndex].coordinates
        self.route = (self.coordinates[0], self.battery[1])
        self.cost = shortestDistance * 9
        battery.capacity -= self.output

    def __str__(self):
        return f"{self.coordinates}, {self.output}, {self.route}, {self.battery}, {self.cost}\n"

class Battery(object):
    """Het model voor de batterij."""

    def __init__(self, x, y, capacity):
        """Initializeert de batterij."""

        self.coordinates = (x, y)
        self.capacity = capacity

    def __str__(self):
        return f"Battery: {self.coordinates}"

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