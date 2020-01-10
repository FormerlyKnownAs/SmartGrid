"""
09-01-2020


Algorithm that connects houses on separate networks to the closest available network node.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from code.algorithms.linetrack import LineTrack

def NearestNetworkV2(houses, networks):

    totalCost = 0
    unconnectedHouses = []

    # Iterates through all houses
    for house in houses:

        # Creates empty list to add distances to and a variable to store coordinates
        distanceList = []
        coordinateList = []
        pointOfConnection = None

        # Iterates through all networks
        for network in networks:

            # Checks network availability
            if network.capacity > house.output:

                # Creates empty list to add coordinates to
                cableDistances = []
                cableLocation = []

                # Iterates through all cables in a network
                for cable in network.cables:

                    # calculates distance between cable and house
                    distanceCable = abs(house.coordinates[0] - cable[0]) + abs(house.coordinates[1] - cable[1])
                    cableDistances.append(distanceCable)
                    cableLocation.append(cable)

                # Finds nearest cable in this network
                shortestCableDistance = min(cableDistances)
                shortestCableIndex = cableDistances.index(shortestCableDistance)

                # adds this distance to longer list
                distanceList.append(shortestCableDistance)
                coordinateList.append(cableLocation[shortestCableIndex])

            else:
                distanceList.append(None)
                coordinateList.append(None)

        # Finds closest cable from network
        if all(i is None for i in distanceList):
            print("hoy")
            unconnectedHouses.append(house)

        else:
            shortestDistance = min(i for i in distanceList if i is not None)
            shortestIndex = distanceList.index(shortestDistance)
            closestNetwork = networks[shortestIndex]

            # Finds all cables
            for cable in LineTrack(house.coordinates, coordinateList[shortestIndex]):
                closestNetwork.cables.add(cable)

            totalCost += shortestDistance * 9
            closestNetwork.capacity -= house.output
            house.connected = True
            
        

    with open("resultaten/networkresults.txt", "w+") as f:
        f.write(f"Unconnected houses: {len(unconnectedHouses)}\n")
        for house in unconnectedHouses:
            f.write(f"{house}\n")

        f.write(F"These houses have been connected:\n")
        for house in houses:
            f.write(f"{house}")

        for network in networks:
            f.write("###################\n")
            f.write(f"This is the network for battery {network.source}.\n")
            f.write(f"End capacity: {network.capacity}\n")
            f.write(f"Cable count: {len(network.cables)}\n")
            f.write("--------------------\n")
            f.write("\nCable Coordinates: \n")

            for cable in network.cables:
                f.write(f"{cable}\n")

    
            


