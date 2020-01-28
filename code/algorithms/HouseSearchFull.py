"""
Algorithm that connects houses on separate networks to the closest available network node.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from code.algorithms.LineTrackRandominput import TrackRandom
import random as r
import os as o
import numpy as np

def NearestHouse(houses, networks):

    totalCost = 0
    cableCost = 9

    r.shuffle(networks)
    filledNetworks = []
    unconnectedHouses = []

    # Loops over all houses
    for i, house in enumerate(houses):

        # Picks an available network, or stores the house in the overflow list if none are available
        curNetID = i % len(networks)
        while curNetID in filledNetworks and len(filledNetworks) < len(networks):
            curNetID = (curNetID + 1) % len(networks)

        # If no networks are available for connection, the house is registered as unconnected
        if len(filledNetworks) >= len(networks):
            unconnectedHouses.append(house)   

        currentNetwork = networks[curNetID]
        chosenHouse = None
        chosenCable = None
        nearestHouseDistance = 10000

        for house in houses:

            #  Checks for capacity and if the house hasn't already been connected
            if currentNetwork.capacity > house.output and house.connected is False:
                
                nearestCableDistance = 10000
                subCable = None
                cableDistances = []

                # Loops over all the cables in the current network
                for cable in currentNetwork.cables:
                    
                    cableDistance = abs(house.coordinates[0] - cable[0]) + abs(house.coordinates[1] - cable[1])
                    cableDistances.append((cableDistance, cable))
                    
                    #  Finds the shortest distance between a house and all the cables
                    if cableDistance < nearestCableDistance:
                        nearestCableDistance = cableDistance
                        subCable = cable

                if nearestCableDistance < nearestHouseDistance:
                    nearestHouseDistance = nearestCableDistance
                    chosenHouse = house
                    chosenCable = subCable

        if chosenHouse is None:
            filledNetworks.append(curNetID)

        # Connects the house with nearest house
        else:
            corner = np.random.randint(2)
            currentNetwork.houses.append(chosenHouse)
            chosenHouse.connected = True
            for cable in TrackRandom(chosenHouse.coordinates, chosenCable, corner):

                currentNetwork.cables.add(cable)
                chosenHouse.cables.append(cable)

            currentNetwork.capacity -= chosenHouse.output
            totalCost += nearestHouseDistance * cableCost

    for house in houses:
        if house.connected is False:
            unconnectedHouses.append(house)

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

    if len(unconnectedHouses) != 0:
        return None

    
    return finalOutput, totalCost, path

