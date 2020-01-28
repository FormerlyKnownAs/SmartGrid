"""

BatterySearch.py

Algorithm that connects houses on separate networks to the 
closest available network. 

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

from code.algorithms.LineTrackRandom import TrackRandom
import random as r
import os as o

def NearestNetwork(houses, networks):
    """ Connects houses on seperate networks to closest
        available network. """

    cableCost = 9
    unconnectedHouses = []

    r.shuffle(houses)
    
    for house in houses:

        # Makes empty list to store distance between house and networkpoint
        distanceList = []

        for network in networks:

            # Checks capacity and if available checks distance to battery
            if network.capacity > house.output:
                distance = abs(house.coordinates[0] - network.source[0]) + 
                            abs(house.coordinates[1] - network.source[1])
                distanceList.append(distance)

            else:
                distanceList.append(None)

        if all(i is None for i in distanceList):
            unconnectedHouses.append(house)

        else:
            # Finds nearest available battery
            shortestDistance = min(i for i in distanceList if i is not None)
            shortestIndex = distanceList.index(shortestDistance)
            chosenNetwork = networks[shortestIndex]

            # Sets battery and route
            house.battery = chosenNetwork.source
            house.route = (house.coordinates[0], house.battery[1])
            house.cost = shortestDistance * cableCost

            chosenNetwork.capacity -= house.output
            chosenNetwork.houses.append(house)

            # Connects the cable between network and house
            for cable in TrackRandom(house.coordinates, chosenNetwork.source):
                chosenNetwork.cables.add(cable)
                house.cables.append(cable)

    # Finds total cost
    totalCables = 0

    for network in networks:
        totalCables += len(network.cables)

    totalCost = totalCables * cableCost

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
