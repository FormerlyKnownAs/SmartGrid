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
from code.algorithms import nearestBatterySimple, nearestNetworkSimple, nearestNetworkv2, nearestNetworkv2random, bestFitNetwork, nearestHouse, nearestNetworkv3random, nearestNetworkShuffle
from code.visualization import visualize

if __name__ == "__main__":
    
    filePrefix = None
    algorithmChoice = None

    try:
        filePrefix = sys.argv[3]
    except:
        filePrefix = "wijk1"

    try:
        algorithmChoice = sys.argv[2]
    except:
        algorithmChoice = 10000

    try:
        repetition = int(sys.argv[1])
    except:
        repetition = 1

    with open("resultaten/simulatieresulaten.txt", "w+") as f:
        
        numberList = []
        unconnectedHouseList = []
        totalCostList = []
        for i in range(repetition):

            houseCSV = f"data/{filePrefix}_huizen.csv"
            batteryCSV = f"data/{filePrefix}_batterijen.csv"

            houseList = house.LoadHouses(houseCSV)
            batteryList = battery.LoadBatteries(batteryCSV)
            networkList = network.LoadNetwork(batteryCSV)

            
            if algorithmChoice == 1:
                nearestBatterySimple.NearestBattery(houseList, batteryList)
            elif algorithmChoice == 2:
                nearestNetworkSimple.NearestNetwork(houseList, networkList)
            elif algorithmChoice == 3:    
                print("Using nearest Network, set")
                nearestNetworkv2.NearestNetworkV2(houseList, networkList)
            elif algorithmChoice == 4:
                print("Using nearest Network, Random")
                results = nearestNetworkv2random.NearestNetworkV2(houseList, networkList, i)
                numberList.append(results[0])
                unconnectedHouseList.append(results[1])
                totalCostList.append(results[2])
                f.write(f"{results[0]}:\n")
                f.write(f"Unconnected Houses: {results[1]}\n")
                f.write(f"Total Cost: {results[2]}\n")
            elif algorithmChoice == 5:
                print("Using BestFit")
                results = bestFitNetwork.BestFit(houseList, networkList, i)
                numberList.append(results[0])
                unconnectedHouseList.append(results[1])
                totalCostList.append(results[2])
                f.write(f"{results[0]}")
                f.write(f"Unconnected Houses: {results[1]}\n")
                f.write(f"Total Cost: {results[2]}\n")
            elif algorithmChoice == 6:
                results = nearestHouse.NearestHouse(houseList, networkList, i)
            elif algorithmChoice == 7:
                results = nearestNetworkv3random.NearestNetworkV3(houseList, networkList, i)
                if results is not None:
                    visualize.Visualize(results[2])
            elif algorithmChoice >= 8:
                results = nearestNetworkv3random.NearestNetworkV3(houseList, networkList, i)
                if results is not None:
                    print("Starting the shuffle")
                    visualize.Visualize(results[2])
                    resultsNew = nearestNetworkShuffle.Shuffle(results[2], results[1])
                    # visualize.Visualize(results[1])

        # f.write("################\n")


        # f.write("results with no unconnected houses:\n")

        # unconnectedHousesLength = 0
        # for i in range(len(unconnectedHouseList)):
        #     if unconnectedHouseList[i] == 0:
        #         f.write(f"{numberList[i]},")
        #         unconnectedHousesLength += 1

        # f.write("\n\nscore for these unconnected house results:\n")        

        # for i in range(len(unconnectedHouseList)):
        #     if unconnectedHouseList[i] == 0:
        #         f.write(f"{totalCostList[i]},")

        # f.write(f"\n{(unconnectedHousesLength / repetition) * 100}% of results have 0 unconnected houses.\n")
        # f.write(f"lowest score is {min(totalCostList)}. Average score is {sum(totalCostList)/len(totalCostList)}.\n")




    