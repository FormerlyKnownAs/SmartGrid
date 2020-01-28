"""

house.py

Houses the House class, also loads houses from a given input files
and generates House objects.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

import csv

class House(object):
    """ The model for House objects."""
    
    def __init__(self, x, y, output):
        """ Initializes a House. """

        self.coordinates = (x, y)
        self.output = output
        self.route = (None, None)
        self.battery = (None, None)
        self.networks = []
        self.cables = []
        self.cost = 0

        # Attributes used for battery first approach
        self.connected = False
        self.distance = 0

    def BatteryCheck(self, batteries):
        """ Checks the best battery based on distance 
            and current capacity. """

        # Makes empty list to store distance between house and battery
        distanceList = []


        for battery in batteries:

            # Checks capacity and if available checks distance to battery
            if battery.capacity > self.output:
                distance = abs(self.coordinates[0] - battery.coordinates[0]) + \
                            abs(self.coordinates[1] - battery.coordinates[1])
                print(f"Self = {self.coordinates}. Battery ="\
                        f"{battery.coordinates}, Capacity = {battery.capacity}")

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
        return f"{self.coordinates}, {self.output}, {self.route}, \
                    {self.battery}, {self.cost}, {self.connected}\n"