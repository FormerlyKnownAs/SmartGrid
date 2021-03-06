"""

BestFitNetwork.py

Algorithm that connects houses to the networks with 
the most remaining capacity.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

from code.algorithms.LineTrackRandom import TrackRandom
import random as r
import os as o

def BestFit(houses, networks):
    """ Connects houses on seperate networks to battery
        that fits it the best.  Takes a list of house objects
        and a list of network objects as argument."""

    totalCost = 0
    cableCost = 9
    unconnectedHouses = []

    r.shuffle(houses)

    # Iterates through the houses
    for house in houses:

        # Creates an empty list to be filled with capacities
        capacityList = []

        for network in networks:
             
            if network.capacity > house.output:

                remainingCapacity = network.capacity - house.output

                capacityList.append(remainingCapacity)

            else:
                capacityList.append(None)

        # Finds closest cable from network
        if all(i is None for i in capacityList):
            unconnectedHouses.append(house)

        else:
            lowestCapacity = min(i for i in capacityList if i is not None)
            lowestCapacityIndex = capacityList.index(lowestCapacity)
            lowestNetwork = networks[lowestCapacityIndex]

            # Creates empty list to add coordinates to
            cableDistances = []
            cableLocation = []

            # Iterates through all cables in best fit network
            for cable in lowestNetwork.cables:

                # Calculates distance between cable and house
                distanceCable = abs(house.coordinates[0] - cable[0]) + \
                                abs(house.coordinates[1] - cable[1])
                cableDistances.append(distanceCable)
                cableLocation.append(cable)
            
            # Finds nearest cable in this network
            shortestCableDistance = min(cableDistances)
            shortestCableIndex = cableDistances.index(shortestCableDistance)

            # Connects the cable between network and house
            for cable in TrackRandom(house.coordinates, 
                                        cableLocation[shortestCableIndex]):
                lowestNetwork.cables.add(cable)
                house.cables.append(cable)

            totalCost += shortestCableDistance * cableCost
            lowestNetwork.capacity -= house.output
            lowestNetwork.houses.append(house)
            house.connected = True

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
            
        
    # Only produces output if there are no unconnected houses left
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
