"""
09-01-2020


Algorithm that connects batteries with the nearest available house.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from code.algorithms.linetrack import LineTrack
import random as r
import os as o

def NearestHouse(houses, networks, id):

    totalCost = 0
    unconnectedHouses = []

    r.shuffle(networks)

    # Iterates through all networks
    for network in networks:

        houseList = []

        for house in houses:

            # Checks for distance is house is unconnected
            if house.connected is False:
            
                distanceHouse = abs(network.source[0] - house.coordinates[0]) + abs(network.source[1] - house.coordinates[1])
                house.distance = distanceHouse
                houseList.append(house)

        houseSorted = sorted(houseList, key=lambda x: x.distance)

        # Connects to the nearest house until capacity threshold of 200 is met
        while network.capacity > 200:

            for i in range(len(houseSorted)):
                network
                

            

