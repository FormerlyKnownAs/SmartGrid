"""
09-01-2020


Algorithm that connects houses on separate networks to the closest available network node.
This functions similarly to v2, but gives a correctly formatted output.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from code.algorithms.LineTrackRandom import TrackRandom
import random as r
import os as o
import json

def NearestHouse(houses, networks, id):

    totalCost = 0
    unconnectedHouses = []
    allCapacities = []

    r.shuffle(networks)

    # Iterates through all houses
    networksClone = networks
    networkIndex = 0
    moduloNum = len(networks)
    while len(houses) > 0 and moduloNum > 0:

        # Selects current network to attach house to
        currentNetwork = networksClone[networkIndex % moduloNum]

        # Finds nearest house
        houseDistance = []
        houseLocation = []
        connectionPoints = []

        for house in houses:

            if house.output < currentNetwork.capacity:
                currentDistance = 1000
                currentCable = None
                for cable in currentNetwork.cables:
                    distance = abs(house.coordinates[0] - cable[0]) + abs(house.coordinates[1] - cable[1])
                    if distance < currentDistance:
                        currentDistance = distance
                        currentCable = cable
                houseDistance.append(currentDistance)
                houseLocation.append(house)
                connectionPoints.append(cable)
            else:
                houseDistance.append(None)
                houseLocation.append(None)
                connectionPoints.append(None)

        # Checks if houses within capacity exist
        if all(i is None for i in houseDistance):
            networksClone.pop(networkIndex % moduloNum)
            allCapacities.append(currentNetwork.capacity)
            moduloNum -= 1

        else:
            houseMinDistance = min(i for i in houseDistance if i is not None)
            houseMinIndex = houseDistance.index(houseMinDistance)

            currentHouse = houseLocation[houseMinIndex]
            bestConnection = connectionPoints[houseMinIndex]

            # Puts down the cable between house and its optimal connection
            for cable in TrackRandom(currentHouse.coordinates, bestConnection):
                currentNetwork.cables.add(cable)
                currentHouse.cables.append(cable)
        

            totalCost += houseMinDistance * 9
            currentNetwork.capacity -= currentHouse.output
            currentNetwork.houses.append(currentHouse)
            currentHouse.connected = True
            houses.pop(houses.index(currentHouse))

        networkIndex += 1

    if moduloNum > 0:
        print("modulo is groter dan nul en we benne klaar")

        # Creates correct output format
        # Finds filename for results
        pathFound = False
        number = 1
        pathName = None
        while pathFound is False:
            path = f"resultaten/networkresults_{number}.json"
            if o.path.exists(path):
                number +=1
            else:
                pathName = path
                pathFound = True

        finalOutput = [{
            "locatie": f"{network.source[0]}, {network.source[1]}",
            "capaciteit": network.capacity,
            "huizen": [
                {
                    "locatie": f"{house.coordinates[0]}, {house.coordinates[1]}",
                    "output": house.output,
                    "kabels": [
                        str(cable) for cable in house.cables
                    ]
                } for house in network.houses
            ]
        } for network in networks]

        return finalOutput, totalCost, path

    return None