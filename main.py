"""
06-01-2020


De functionaliteit.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

import sys
import csv
import re
import random as r

from code.classes import house, battery, network
from code.algorithms import nearestBatterySimple, nearestNetworkSimple, nearestNetworkv2, nearestNetworkv2random, bestFitNetwork, nearestHouse, nearestNetworkv3random, nearestNetworkShuffle, nearestNetworkSort
from code.visualization import visualize

def main(filePrefix, algorithmChoice, repetition):
    """
        Chooses the file, function and repetition, and sends the output to the visualizer.
    """

    # Opens the results file to possibly write results in
    with open("resultaten/simulatieresulaten.txt", "w+") as f:
        
        # Sets the information to be called upon later
        numberList = []
        unconnectedHouseList = []
        totalCostList = []

        # Loads in the data types
        houseCSV = f"data/{filePrefix}_huizen.csv"
        batteryCSV = f"data/{filePrefix}_batterijen.csv"
        houseList = house.LoadHouses(houseCSV)
        batteryList = battery.LoadBatteries(batteryCSV)
        networkList = network.LoadNetwork(batteryCSV)

        # Chooses the algorithm
        for i in range(repetition):

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
            elif algorithmChoice == 8:
                results = nearestNetworkv3random.NearestNetworkV3(houseList, networkList, i)
                if results is not None:
                    baseCost = results[1]
                    print("Starting the sort")
                    visualize.Visualize(results[2])
                    j = 0
                    k = 0
                    allResults = []
                    allCostResults = []
                    while j < 100 and k < 500:
                        resultsNew = nearestNetworkShuffle.Shuffle(results[2], results[1])
                        allCostResults.append(resultsNew[1])
                        allResults.append(resultsNew)
                        k += 1
                        if resultsNew[1] < baseCost:
                            j += 1

                    # Gets information of run
                    print(f"best Change: {min(allCostResults)}, total of {baseCost - min(allCostResults)}\nworst Change: {max(allCostResults)}, total of {baseCost - max(allCostResults)}\naverage change: {baseCost - (sum(allCostResults) / len(allCostResults))}.\n Total attempts: {k}, unsuccessful ones = {k - j}")
                    
                    # Visualizes best result
                    visualize.Visualize(allResults[allCostResults.index(min(allCostResults))][2])
            elif algorithmChoice == 9:
                results = nearestNetworkv3random.NearestNetworkV3(houseList, networkList, i)
                if results is not None:
                    baseCost = results[1]
                    print("Starting the sort")
                    visualize.Visualize(results[2])
                    j = 0
                    k = 0
                    allResults = []
                    allCostResults = []
                    while j < 500:
                        resultsNew = nearestNetworkSort.Sort(results[2], results[1])
                        allCostResults.append(resultsNew[1])
                        allResults.append(resultsNew)
                        k += 1
                        if resultsNew[1] < baseCost:
                            j += 1

                    # Gets information of run
                    print(f"best Change: {min(allCostResults)}, total of {baseCost - min(allCostResults)}\nworst Change: {max(allCostResults)}, total of {baseCost - max(allCostResults)}\naverage change: {baseCost - (sum(allCostResults) / len(allCostResults))}.\n Total attempts: {k}, unsuccessful ones = {k - j}")
                    
                    # Visualizes best result
                    visualize.Visualize(allResults[allCostResults.index(min(allCostResults))][2])
            elif algorithmChoice >= 10:
                results = nearestNetworkv3random.NearestNetworkV3(houseList, networkList, i)
                if results is not None:
                    baseCost = results[1]
                    print("starting the shuffle & sort")
                    visualize.Visualize(results[2])
                    j = 0
                    totalRuns = 0
                    sortRuns = 0
                    shuffleRuns = 0
                    allResults = []
                    allCostResults = []
                    while j < 100:
                        optimizerChoice = r.randint(1, 2)

                        if optimizerChoice == 1:
                            resultsNew = nearestNetworkShuffle.Shuffle(results[2], results[1])
                            shuffleRuns += 1
                        else:
                            resultsNew = nearestNetworkSort.Sort(results[2], results[1])
                            sortRuns += 1

                        allCostResults.append(resultsNew[1])
                        allResults.append(resultsNew)
                        totalRuns += 1
                        if resultsNew[1] < baseCost:
                            j += 1

                    # Gets information of run
                    print(f"did {totalRuns} runs. {shuffleRuns} were shuffled, {sortRuns} were sorted")
                    print(f"best Change: {min(allCostResults)}, total of {baseCost - min(allCostResults)}\nworst Change: {max(allCostResults)}, total of {baseCost - max(allCostResults)}\naverage change: {baseCost - (sum(allCostResults) / len(allCostResults))}.\n Total attempts: {totalRuns}, unsuccessful ones = {totalRuns - j}")
                    
                    # Visualizes best result
                    visualize.Visualize(allResults[allCostResults.index(min(allCostResults))][2])

if __name__ == "__main__":

    # Sets the parameters of the function based on the input, and creates default values
    try:
        filePrefix = sys.argv[3]
    except:
        filePrefix = "wijk1"

    try:
        algorithmChoice = int(sys.argv[2])
    except:
        algorithmChoice = 10000

    try:
        repetition = int(sys.argv[1])
    except:
        repetition = 1

    main(filePrefix, algorithmChoice, repetition)




    