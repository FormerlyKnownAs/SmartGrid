"""

HouseSearchHybrid.py

Algorithm that connects houses on separate networks to the closest 
available network node. This functions similarly to v2, 
but gives a correctly formatted output.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

from code.algorithms.LineTrackRandominput import TrackRandom
import random as r
import os as o
import numpy as np

def NearestHouse(houses, networks):
    """ Connects houses on seperate networks to closest network
        node in correctly formatted output. Takes a list of 
        house objects and a list of network objects as argument."""

    totalCost = 0

    cableCost = 9
    r.shuffle(networks)
    filledNetworks = []
    unconnectedHouses = []
    connectedHouses = []

    # Loops over all houses except the last 10
    for i in range(len(houses) - 10):

        # Picks an available network, or stores the house 
        # in the overflow list if none are available
        curNetID = i % len(networks)
        while curNetID in filledNetworks and \
                len(filledNetworks) < len(networks):
            curNetID = (curNetID + 1) % len(networks)
        
        # If no networks are available for connection, 
        # the house is registered as unconnected
        if len(filledNetworks) >= len(networks):
            unconnectedHouses.append(house)   

        currentNetwork = networks[curNetID]
        chosenHouse = None
        chosenCable = None
        nearestHouseDistance = 10000

        for house in houses:
            
            #  Checks for capacity and if the house hasn't already been 
            #  connected
            if currentNetwork.capacity > house.output and \
                                    house.connected is False:
                
                nearestCableDistance = 10000
                subCable = None
                cableDistances = []
                for cable in currentNetwork.cables:
                    
                    cableDistance = abs(house.coordinates[0] - cable[0]) + \
                                    abs(house.coordinates[1] - cable[1])
                    cableDistances.append((cableDistance, cable))

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
            currentNetwork.houses2.add(chosenHouse)
            chosenHouse.connected = True
            chosenHouse.networks.append(currentNetwork)
            connectedHouses.append(chosenHouse)
            for cable in TrackRandom(chosenHouse.coordinates, 
                                        chosenCable, corner):

                currentNetwork.cables.add(cable)
                chosenHouse.cables.append(cable)

            currentNetwork.capacity -= chosenHouse.output
            totalCost += nearestHouseDistance * cableCost

    # After the first amount of houses, places the last few houses 
    # randomly rather than based on distance to network
    r.shuffle(houses)

    for house in houses:
        
        # Only accepts houses that are not connected
        if house.connected is False:
            closestNetworkPoint = []
            closestPointDistance = []

            for network in networks:

                if house.output < network.capacity:
                    
                    nearestCable = None
                    nearestCableDistance = 10000

                    # Finds the shortest distance to a cable 
                    # for a house to connect to
                    for cable in network.cables:
                        cableDistance = abs(house.coordinates[0] - cable[0]) + \
                                        abs(house.coordinates[1] - cable[1])
                        if cableDistance < nearestCableDistance:
                            nearestCable = cable
                            nearestCableDistance = cableDistance
                        
                    closestNetworkPoint.append(nearestCable)
                    closestPointDistance.append(nearestCableDistance)
                    
                else:
                    closestNetworkPoint.append(None)
                    closestPointDistance.append(None)

            # If no connections are available appends the house to the 
            # unconnectedhouses list
            if all(i is None for i in closestPointDistance):
                unconnectedHouses.append(house)

            # Otherwise looks for the shortest distance, finds the index 
            # for the network belonging to that distance
            else:        
                shortestDistance = min(i for i in closestPointDistance if 
                                                            i is not None)
                shortestIndex = closestPointDistance.index(shortestDistance)
                closestNetwork = networks[shortestIndex]

                # Finds all cables
                corner = np.random.randint(2)
                closestNetwork.houses2.add(house)
                house.networks.append(closestNetwork)
                closestNetwork.capacity -= house.output
                house.connected = True
                connectedHouses.append(house)
                
                # Adds the cables to make a connection to the 
                # found network point
                for cable in TrackRandom(house.coordinates, 
                            closestNetworkPoint[shortestIndex], corner):
                    closestNetwork.cables.add(cable)
                    house.cables.append(cable)
 
                totalCost += shortestDistance * cableCost
    
    # Prevents multiple cables from the same network 
    # being drawn on the same point
    allhouses = 0
    for network in networks:
        allhouses += len(network.houses2)
        for house in network.houses2:
            network.houses.append(house)

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

