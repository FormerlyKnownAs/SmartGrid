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

    def BatteryCheck(self, batteries):
        """Checks the best battery based on distance and current capacity."""

        # Makes empty list to store distance between house and battery
        distanceList = []


        for battery in batteries:

            # Checks capacity and if available checks distance to battery
            if battery.capacity > self.output:
                distance = abs(self.coordinates[0] - battery.coordinates[0]) + abs(self.coordinates[1] - battery.coordinates[1])
                print(f"Self = {self.coordinates}. Battery = {battery.coordinates}")

                distanceList.append(distance)
            else:
                distanceList.append(None)

        # Finds nearest available battery
        print(f"{distanceList}, hey")
        shortestDistance = min(i for i in distanceList if i is not None)
        print(shortestDistance)
        shortestIndex = distanceList.index(shortestDistance)

        # Sets battery and route
        self.battery = batteries[shortestIndex].coordinates
        self.route = (self.coordinates[0], self.battery[1])
        battery.capacity -= self.output

    def __str__(self):
        return f"{self.coordinates}, {self.output}, {self.route}, {self.battery}\n"

class Battery(object):
    """Het model voor de batterij."""

    def __init__(self, x, y, capacity):
        """Initializeert de batterij."""

        self.coordinates = (x, y)
        self.capacity = capacity

    def __str__(self):
        return f"Battery: {self.coordinates}"
