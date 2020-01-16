"""
09-01-2020

Takes a json file and keeps its connections, but reconfiguring its connections based on distance

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from code.algorithms.LineTrackRandom import TrackRandom
import random as r
import os as o
import json

def Sort(inputFile, previousScore):

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
        sourceCable = (int(sourceCable[0]), int(sourceCable[1]))
        cables.add(sourceCable)

        # Finds all houses associated with network
        for house in network["huizen"]:
            house["kabels"] = []
            coordinatesHouse = house["locatie"].split(",")
            coordinatesHouse = (int(coordinatesHouse[0]), int(coordinatesHouse[1]))
            house["distance"] = abs(coordinatesHouse[0] - sourceCable[0]) + abs(coordinatesHouse[1] - sourceCable[1])
            houseList.append(house)

        houseList = sorted(houseList, key=lambda x: x["distance"])

        # Finds closest point on network for each house
        for house in houseList:
            
            cableDistance = []
            cableLocation = []
            coordinatesHouse = house["locatie"].split(",")
            coordinatesHouse = (int(coordinatesHouse[0]), int(coordinatesHouse[1]))

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
                "kabels": [
                    str(cable) for cable in house["kabels"]
                ]
            } for house in network["huizen"]
        ]
    } for network in json_dict]

    with open(f"{inputFile}shuffle.json", "w+") as f:
        json.dump(finalOutput, f, indent=4)

    print(f"Originally: {previousScore}, now: {totalCost}")

    return finalOutput, totalCost, f"{inputFile}shuffle.json"



            
        
