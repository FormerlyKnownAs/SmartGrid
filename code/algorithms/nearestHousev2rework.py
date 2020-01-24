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

def NearestHouse(houses, networks):

    totalCost = 0

    r.shuffle(networks)

    
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

