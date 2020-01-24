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
import copy
import json

def NearestHouse(houses, networks, id):

    totalCost = 0
    unconnectedHouses = []
    allCapacities = []

    r.shuffle(networks)

    # Iterates through all houses
    networksClone = copy.copy(networks)
    housesClone = copy.copy(houses)
    networkIndex = 0
    moduloNum = len(networks)

    while len(housesClone) > 0 and moduloNum > 0:

        # Selects current network to attach house to
        currentNetwork = networksClone[networkIndex % moduloNum]
        print(f"cables associated with this network: {len(currentNetwork.cables)}")
        # Finds nearest house
        houseDistance = []
        houseLocation = []
        connectionPoints = []

        for house in housesClone:

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
            print(f"len of current houses = {len(currentNetwork.houses)}")
            currentHouse.connected = True
            housesClone.pop(housesClone.index(currentHouse))

        networkIndex += 1

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

    print(f"network length is {len(networks)}")
    totalconnectedhouses = 0
    for network in networks:
        print(f"{len(network.houses)} is len, {network.capacity} is capacity.")
        totalconnectedhouses += len(network.houses)

    print(f"unconnected houses = {150 - totalconnectedhouses}")
    for house in houses:
        if house.connected is False:
            unconnectedHouse = house
            print(house)

    for network in networks:
        totalHouseCable = 0
        for house in network.houses:
            totalHouseCable += len(house.cables)
        print(f"Length of total cable = {len(network.cables)}, totalHouseCable = {totalHouseCable}. dif = {len(network.cables) - totalHouseCable}")


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

    totalhouses = 0
    for network in networks:
        totalhouses += len(network.houses)
    print(totalhouses)

    return finalOutput, totalCost, path

