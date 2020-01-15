"""
09-01-2020

Takes a json file and keeps its connections, but shuffling its cable connections.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from code.algorithms.LineTrackRandom import TrackRandom
import random as r
import os as o
import json

def Shuffle(inputFile, previousScore):

    # Set variables to be measured
    totalCost = 0

    # Load JSON file
    with open(inputFile, 'r') as JSON:
        json_dict = json.load(JSON)

    # Declare the conversion lists
    newJSON = []
    
    for network in json_dict:

        houseList = []
        cables = set()

        # Sets the battery as the first cable
        sourceCable = network["locatie"].strip("()").split(",")
        cables.add((int(sourceCable[0]), int(sourceCable[1])))

        # Finds all houses associated with network
        for house in network["huizen"]:
            houseList.append(house)
            house["kabels"] = []

        r.shuffle(houseList)

        # Finds closest point on network for each house
        for house in houseList:
            
            cableDistance = []
            cableLocation = []

            coordinatesHouse = house["locatie"].strip("()").split(",")
            coordinatesHouse = (int(coordinatesHouse[0]), int(coordinatesHouse[0]))

            for cable in cables:

                # calculates distance between cable and house
                distanceCable = abs(coordinatesHouse[0] - cable[0]) + abs(coordinatesHouse[1] - cable[1])
                cableDistance.append(distanceCable)
                cableLocation.append(cable)

            # Finds nearest cable in this network
            shortestCableDistance = min(cableDistance)
            shortestCableIndex = cableDistance.index(shortestCableDistance)

            # Connect the house to the nearest cable
            for cable in TrackRandom(coordinatesHouse, cableLocation[shortestCableIndex]):
                cables.add(cable)
                house["kabels"].append(cable)

            totalCost += shortestCableDistance * 9

    print(f"Originally: {previousScore}, now: {totalCost}")



            
        
