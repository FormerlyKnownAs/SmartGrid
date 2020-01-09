"""
06-01-2020


De functionaliteit.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

import sys
from models import Battery, House
import csv
import re

if __name__ == "__main__":

    # Sets file names
    filePrefix = sys.argv[1]
    outputFile = sys.argv[2]

    # Makes empty lists to be filled with csv data
    houseList = []
    networkList = []

    # Makes empty dictionairy for the network
    cablesDict = {}
    batterCapacity = {}



    # Reads battery data
    with open(f"data/{filePrefix}_batterijen.csv", "r") as f:
        
        # Skips header
        csvreader = csv.reader(f)
        next(csvreader, None)
        networkNumber = 1
        # Reads the lines
        for line in f:

            # Makes an empty list to append battery data to
            networkData = []

            # Splits the data per line
            for element in line.split(","):

                # Reads out numbers and stores them as floats
                element = element.strip('"[]"')
                networkData.append(float(element))

            # Makes battery object and adds to list

            newNetwork = Network(networkData[0], networkData[1], networkData[2])
            networkList.append(newNetwork)

            # Adds the individual networks and their positioning to the cables dictionairy.
            cablesDict[networkNumber] = (networkData[0], networkData[1])
            batteryCapacity[networkNumber] = networkData[2]
            networkNumber += 1

    # Reads house data
    with open(f"data/{filePrefix}_huizen.csv", "r") as f:

        # Skips header
        csvreader = csv.reader(f)
        next(csvreader, None)

        # Reads the lines
        for line in f:

            # Makes an empty list to append house data to
            houseData = []

            # Splits the data per line
            for element in line.split(","):

                # Reads out numbers and stores them as floats
                houseData.append(float(element))

            # Makes house object and adds to list
            newHouse = House(houseData[0], houseData[1], houseData[2])
            houseList.append(newHouse)
    
    for house in houseList:
            house.BatteryCheck(cablesDict,batteryCapacity)
    

    totalCost = 0

    

    # with open("paths.txt","w+") as f:

    #     f.write("coordinates, output, route, battery, cost\n")

    #     for house in houseList:
    #         house.BatteryCheck(cablesDict,batteryCapacity)
    #         f.write(f"{house}")
    #         totalCost += house.cost
    
    # with open("results.txt", "w+") as f:

    #     f.write(f"Results for {filePrefix}.\n\n")
    #     f.write(f"Total Distance of Cable = €{totalCost / 9}\n")
    #     f.write(f"Total Cost of Cable = €{totalCost}\n")

    #     allCost = len(batteryList) * 5000 + totalCost
    #     f.write(f"Total cost = €{allCost}\n")




# with open(nodes_file, 'r') as in_file:
#             reader = csv.DictReader(in_file)
#             nodes = {}


#             for row in reader:
#                 nodes[row['id']] = Node(row['name'], row['id'])

#         return nodes




            # for row in reader:
            #     neighbours = [neighbour.strip('[] ' for neighbour in 
            #                   row['neighbours'].split(',') if neighbour.strip('[] ') != '')]