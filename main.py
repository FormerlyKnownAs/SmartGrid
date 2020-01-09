"""
06-01-2020


De functionaliteit.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

import sys
import csv
import re
import random

from code.classes import house, battery, network
from code.algorithms import nearestBatterySimple

if __name__ == "__main__":
    
    filePrefix = sys.argv[1]
    outputFile = sys.argv[2]

    houseCSV = f"data/{filePrefix}_huizen.csv"
    batteryCSV = f"data/{filePrefix}_batterijen.csv"

    houseList = house.LoadHouses(houseCSV)
    batteryList = battery.LoadBatteries(batteryCSV)
    networkList = network.LoadNetwork(batteryCSV)

    nearestBatterySimple.NearestBattery(houseList, batteryList)


    