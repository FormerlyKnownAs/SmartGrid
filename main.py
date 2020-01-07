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
    batteryList = []


    # Reads battery data
    with open(f"data/{filePrefix}_batterijen.csv", "r") as f:
        
        # Skips header
        csvreader = csv.reader(f)
        next(csvreader, None)

        # Reads the lines
        for line in f:

            # Makes an empty list to append battery data to
            batteryData = []

            # Splits the data per line
            for element in line.split(","):

                # Reads out numbers and stores them as floats
                element = element.strip('"[]"')
                batteryData.append(float(element))

            # Makes battery object and adds to list
            newBattery = Battery(batteryData[0], batteryData[1], batteryData[2])
            batteryList.append(newBattery)
    
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
    
    totalCost = 0

    with open("paths.txt","w+") as f:

        f.write("coordinates, output, route, battery, cost\n")

        for house in houseList:
            house.BatteryCheck(batteryList)
            f.write(f"{house}")
            totalCost += house.cost
    
    with open("results.txt", "w+") as f:

        f.write(f"Results for {filePrefix}.\n\n")
        f.write(f"Total Distance of Cable = €{totalCost / 9}\n")
        f.write(f"Total Cost of Cable = €{totalCost}\n")

        allCost = len(batteryList) * 5000 + totalCost
        f.write(f"Total cost = €{allCost}\n")

