"""

CornerChange.py

Generates a set of turns and changes them.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

from code.algorithms.LineTrackRandominput import TrackRandom
import random as r
import os as o
import json

def hillSort(inputFile, previousScore, randomizationList):
    """ Generates a set of turns and changes them. """

    # Set variables to be measured
    totalCost = 0

    cableCost = 9

    # Load JSON file
    with open(inputFile, 'r') as JSON:
        json_dict = json.load(JSON)

    # Makes one random change in the inputfile
    randomNetwork = json_dict[r.randint(0, len(json_dict) - 1)]
    randomHouse = randomNetwork["huizen"][r.randint(0, 
                            len(randomNetwork["huizen"]) - 1)]
    if randomHouse["corner"] == 0:
        randomHouse["corner"] = 1
    else:
        randomHouse["corner"] = 0

    networkID = 0
    for network in json_dict:

        houseList = []
        cables = set()

        # Sets the battery as the first cable
        sourceCable = network["locatie"].strip("()").split(",")
        sourceCable = (int(sourceCable[0]), int(sourceCable[1]))
        cables.add(sourceCable)

        # Finds all houses associated with network
        houseId = 0
        for house in network["huizen"]:
            house["kabels"] = []
            coordinatesHouse = house["locatie"].split(",")
            coordinatesHouse = (int(coordinatesHouse[0]), 
                                int(coordinatesHouse[1]))
            house["distance"] = abs(coordinatesHouse[0] - sourceCable[0]) + \
                                abs(coordinatesHouse[1] - sourceCable[1])
            houseList.append(house)

        # Sorts the houses based on distance to battery
        houseList = sorted(houseList, key=lambda x: x["distance"])

        # Finds closest point on network for each house
        for house in houseList:
            
            cableDistance = []
            cableLocation = []
            coordinatesHouse = house["locatie"].split(",")
            coordinatesHouse = (int(coordinatesHouse[0]), 
                                int(coordinatesHouse[1]))

            for cable in cables:

                # calculates distance between cable and house
                distanceCable = abs(coordinatesHouse[0] - cable[0]) + \
                                abs(coordinatesHouse[1] - cable[1])
                cableDistance.append(distanceCable)
                cableLocation.append(cable)

            # Finds nearest cable in this network
            shortestCableDistance = min(cableDistance)
            shortestCableIndex = cableDistance.index(shortestCableDistance)

            # Connect the house to the nearest cable
            for cable in TrackRandom(coordinatesHouse, 
                        cableLocation[shortestCableIndex], house["corner"]):
                cables.add(cable)
                house["kabels"].append(cable)

            totalCost += shortestCableDistance * cableCost
            houseId += 1

        networkID += 1

    # Creates correct output format
    # Finds filename for results
    inputFile = inputFile.strip(".json")
            
    finalOutput = [{
        "locatie": network["locatie"],
        "capaciteit": network["capaciteit"],
        "huizen": [
            {
                "locatie": house["locatie"],
                "output": house["output"],
                "corner": house["corner"],
                "kabels": [
                    str(cable) for cable in house["kabels"]
                ]
            } for house in network["huizen"]
        ]
    } for network in json_dict]

    return finalOutput, totalCost, f"{inputFile}.json", randomizationList, \
                                                                    houseList



            
        
