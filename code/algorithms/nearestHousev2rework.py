"""
09-01-2020


Algorithm that connects houses on separate networks to the closest available network node.
This functions similarly to v2, but gives a correctly formatted output.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from code.algorithms.LineTrackRandominput import TrackRandom
import random as r
import os as o
import numpy as np
import copy
import json

def NearestHouse(houses, networks):

    totalCost = 0

    r.shuffle(networks)
    filledNetworks = []
    unconnectedHouses = []

    for i, house in enumerate(houses):

        # Picks an available network, or stores the house in the overflow list if none are available
        curNetID = i % len(networks)
        while curNetID in filledNetworks and len(filledNetworks) < len(networks):
            curNetID = (curNetID + 1) % len(networks)
        if len(filledNetworks) >= len(networks):
            unconnectedHouses.append(house)   

        currentNetwork = networks[curNetID]
        chosenHouse = None
        chosenCable = None
        nearestHouseDistance = 10000

        for house in houses:

            if currentNetwork.capacity > house.output and house.connected is False:
                
                nearestCableDistance = 10000
                cableDistances = []
                for cable in currentNetwork.cables:
                    
                    cableDistance = abs(house.coordinates[0] - cable[0]) + abs(house.coordinates[1] - cable[1])
                    cableDistances.append((cableDistance, cable))

                    if cableDistance < nearestCableDistance:
                        nearestCableDistance = cableDistance
                        chosenCable = cable

                if nearestCableDistance < nearestHouseDistance:
                    nearestHouseDistance = nearestCableDistance
                    chosenHouse = house

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

            totalCost += nearestHouseDistance * 9
            print(f"connected {chosenHouse.coordinates} to {chosenCable}. It has been added to {curNetID}. {filledNetworks}")
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

