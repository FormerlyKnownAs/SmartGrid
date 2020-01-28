"""

TrueRandom.py

Purely random algorithm, used for score reference. 

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

from code.algorithms.LineTrackRandom import TrackRandom
import random as r
import os as o

def RandomConnect(houses, networks):

    cableCost = 9

    unconnectedHouses = []

    r.shuffle(houses)
    
    for house in houses:

        # Makes empty list to store distance between house and networkpoint
        availabilityList = []

        for network in networks:

            # Checks capacity and if available checks distance to battery
            if network.capacity > house.output:
                availabilityList.append(network)


        if len(availabilityList) <= 0:
            unconnectedHouses.append(house)

        else:
            randomNetwork = availabilityList[r.randint(0, 
                                    len(availabilityList) - 1)]


            # Sets battery and route
            house.battery = randomNetwork.source
            house.route = (house.coordinates[0], house.battery[1])

            randomNetwork.capacity -= house.output
            randomNetwork.houses.append(house)

            # Connects the cable between network and house
            for cable in TrackRandom(house.coordinates, randomNetwork.source):
                randomNetwork.cables.add(cable)
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
