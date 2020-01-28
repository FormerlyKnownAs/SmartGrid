"""

CornerPositionChange.py

Takes previous input data and changes one element, 
be it a randomized corner or the location of a house.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

from code.algorithms.LineTrackRandominput import TrackRandom
import random as r
import numpy as np
import os as o
import json

def hillSort(inputFile, previousScore, randomizationList):
    """ Changes one element in input, corner or
        house location. """

    # Set variables to be measured
    totalCost = 0

    # Load JSON file
    with open(inputFile, 'r') as JSON:
        json_dict = json.load(JSON)

    # Makes one random change in the inputfile
    randomNetwork = json_dict[r.randint(0, len(json_dict) - 1)]
    randomHouseIndex = r.randint(0, len(randomNetwork["huizen"]) - 1)
    randomHouse = randomNetwork["huizen"][randomHouseIndex ]

    #  Makes a random choice between 0 and 1
    randomChoice = r.randint(0, 1)

    # Changes either the corner layout or moves a house in order 
    # depending on randomChoice
    if randomChoice == 1:
        
        if randomHouse["corner"] == 0:
            randomHouse["corner"] = 1
        else:
            randomHouse["corner"] = 0
    else:
        changeIndex = 0

        while changeIndex <= 0 or changeIndex > 
                                len(randomNetwork["huizen"]) - 1:
            changeIndex = r.randint(-3, 3) + randomHouseIndex

        randomNetwork["huizen"].pop(randomHouseIndex)
        randomNetwork["huizen"].insert(changeIndex, randomHouse)



    networkID = 0

    # Loops over every network
    for network in json_dict:

        houseList = []
        cables = set()

        # Sets the battery as the first cable
        sourceCable = network["locatie"].strip("()").split(",")
        sourceCable = (int(sourceCable[0]), int(sourceCable[1]))
        cables.add(sourceCable)

        # Finds all houses associated with network and appends them to the houseList
        for house in network["huizen"]:
            house["kabels"] = []
            coordinatesHouse = house["locatie"].split(",")
            coordinatesHouse = (int(coordinatesHouse[0]), 
                                int(coordinatesHouse[1]))
            house["distance"] = abs(coordinatesHouse[0] - sourceCable[0]) + 
                                abs(coordinatesHouse[1] - sourceCable[1])
            houseList.append(house)

        # Finds closest point on network for each house
        while len(houseList) > 0:
            
            # Finds nearest house
            houseDistance = []
            houseLocation = []
            for house in houseList:

                # Corrects the input for further calculation
                coordinatesHouse = house["locatie"].split(",")
                coordinatesHouse = (int(coordinatesHouse[0]), 
                                    int(coordinatesHouse[1]))

                currentDistance = 1000

                # Finds the shortest distance from all known cable locations
                for cable in cables:
                   distance = abs(coordinatesHouse[0] - cable[0]) + 
                                abs(coordinatesHouse[1] - cable[1])
                   if distance < currentDistance:
                       currentDistance = distance
                houseDistance.append(currentDistance)
                houseLocation.append(house)

            # Takes the shortest distance from houseDistance list
            houseMinimalDistance = min(houseDistance)

            # Finds the index of the shortest distance and then is able to find
            # the house associated with that distance
            indexHouseMinimalDistance = houseDistance.index(houseMinimalDistance)
            currentHouse = houseLocation[indexHouseMinimalDistance]


            # Once house is found, put down cables
            cableDistance = []
            cableLocation = []
            coordinatesHouse = currentHouse["locatie"].split(",")
            coordinatesHouse = (int(coordinatesHouse[0]), 
                                int(coordinatesHouse[1]))

            for cable in cables:

                # calculates distance between cable and house
                distanceCable = abs(coordinatesHouse[0] - cable[0]) + 
                                abs(coordinatesHouse[1] - cable[1])
                cableDistance.append(distanceCable)
                cableLocation.append(cable)

            # Finds nearest cable in this network
            shortestCableDistance = min(cableDistance)
            shortestCableIndex = cableDistance.index(shortestCableDistance)

            # Connect the house to the nearest cable
            corner = np.random.randint(2)
            currentHouse["corner"] = corner
            for cable in TrackRandom(coordinatesHouse, 
                                cableLocation[shortestCableIndex], corner):
                cables.add(cable)
                currentHouse["kabels"].append(cable)

            totalCost += shortestCableDistance * 9

            # Find index of current house in houselist
            houseListIndex = houseList.index(currentHouse)
            houseList.pop(houseListIndex)

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

    return finalOutput, totalCost, f"{inputFile}sort.json", houseList



            