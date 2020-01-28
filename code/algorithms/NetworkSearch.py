"""

NetworkSearch.py

Algorithm that connects houses on separate networks to the closest available network node.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

from code.algorithms.LineTrackRandom import TrackRandom
import random as r
import os as o
import json

def NearestNetworkV3(houses, networks, id):

    totalCost = 0
    unconnectedHouses = [] 

    r.shuffle(houses)

    # Iterates through all houses
    for house in houses:

        # Creates empty list to add distances to and a variable to store coordinates
        distanceList = []
        coordinateList = []
        pointOfConnection = None

        # Iterates through all networks
        for network in networks:

            # Checks network availability
            if network.capacity > house.output:

                # Creates empty list to add coordinates to
                cableDistances = []
                cableLocation = []

                # Iterates through all cables in a network
                for cable in network.cables:

                    # calculates distance between cable and house
                    distanceCable = abs(house.coordinates[0] - cable[0]) + abs(house.coordinates[1] - cable[1])
                    cableDistances.append(distanceCable)
                    cableLocation.append(cable)

                # Finds nearest cable in this network
                shortestCableDistance = min(cableDistances)
                shortestCableIndex = cableDistances.index(shortestCableDistance)

                # adds this distance to longer list
                distanceList.append(shortestCableDistance)
                coordinateList.append(cableLocation[shortestCableIndex])

            else:
                distanceList.append(None)
                coordinateList.append(None)

        # Finds closest cable from network
        if all(i is None for i in distanceList):
            unconnectedHouses.append(house)

        else:
            shortestDistance = min(i for i in distanceList if i is not None)
            shortestIndex = distanceList.index(shortestDistance)
            closestNetwork = networks[shortestIndex]

            # Finds all cables
            for cable in TrackRandom(house.coordinates, coordinateList[shortestIndex]):
                closestNetwork.cables.add(cable)
                house.cables.append(cable)

            totalCost += shortestDistance * 9
            closestNetwork.capacity -= house.output
            closestNetwork.houses.append(house)
            house.connected = True

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

    if len(unconnectedHouses) == 0:

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
    