"""
06-01-2020


De functionaliteit.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

import sys
import random as r
import json

from code.classes import house, network
from code.algorithms import BatterySearch, bestFitNetwork, CornerChange, CornerPositionChange, HouseSearchFull, HouseSearchHybrid, NetworkSearch, ResultsDynamicSort, ResultShuffle, ResultsSort, TrueRandom
from code.visualization import visualize

def main(filePrefix, algorithmChoice, iterations):
    """
        Chooses the file, function and repetition, and sends the output to the visualizer.
    """

    if algorithmChoice == 1:
        result = HillClimb(Optimize(Random(filePrefix, iterations, 1), iterations * 2, 1), iterations * 4)
    elif algorithmChoice == 2:
        result = HillClimb(Optimize(Random(filePrefix, iterations, 1), iterations * 2, 1), iterations * 4, True)
    elif algorithmChoice == 3:
        result = HillClimb(Optimize(Random(filePrefix, iterations, 1), iterations * 2, 2), iterations * 4)
    elif algorithmChoice == 4:
        result = HillClimb(Optimize(Random(filePrefix, iterations, 1), iterations * 2, 2), iterations * 4, True)
    elif algorithmChoice == 5:
        results = HillClimb(Optimize(Random(filePrefix, iterations, 1), iterations * 2, 2), iterations * 4, True)
    elif algorithmChoice == 6:
        results = Random(filePrefix, iterations, 3)
    elif algorithmChoice >= 7 or algorithmChoice < 1:
        results = Random(filePrefix, iterations, 6)
        
    
        
def readinInfo(filePrefix, networkBool):
    """
    Reads in the csv files for the neighborhoods.
    """
    houseList = house.LoadHouses(f"data/{filePrefix}_huizen.csv")
    if networkBool:
        networkList = network.LoadNetwork(f"data/{filePrefix}_batterijen.csv")

        return houseList, networkList

    batteryList = battery.LoadBatteries(f"data/{filePrefix}_batterijen.csv")

    return houseList, batteryList

def ScoreCheck(newResults, previousResults, failedImprovements):
    """
    Compares scores, increments counter and returns the better result.
    """

    if newResults is not None:
        if newResults[1] < previousResults[1]:
            failedImprovements = 0
            print(f"prev = {previousResults[1]}, new = {newResults[1]}")
            return failedImprovements, newResults
        else:
            failedImprovements += 1
            if failedImprovements % 50 == 0:
                print(failedImprovements)

            return failedImprovements, previousResults

    return failedImprovements, previousResults

def VisualJSON(result, previousResult=None):
    """
    Creates a JSON file and visualizes the result. If a previousResult is given, creates an underlay. 
    """

    with open(result[2], "w+") as f:
        json.dump(result[0], f, indent=4)

    if previousResult is not None:
        visualize.Visualize(previousResult[2], True)
    visualize.Visualize(result[2])

def Random(filePrefix, iterations, subChoice):
    """
    Runs the NearestNetworkV3 random algorithm as many times as iterations, and returns the best result.
    """

    runCounter = 0
    failedImprovements = 0
    bestScore = 1000
    bestRandom = None

    while failedImprovements < iterations:

        runCounter += 1
        houseList, networkList = readinInfo(filePrefix, True)
        
        if subChoice == 1:
            results = NetworkSearch.NearestNetworkV3(houseList, networkList, 1)
        if subChoice == 2:
            results = HouseSearchHybrid.NearestHouse(houseList, networkList)
        if subChoice == 3:
            results = HouseSearchFull.NearestHouse(houseList, networkList)
        if subChoice == 4:
            results = bestFitNetwork.BestFit(houseList, networkList)
        if subChoice == 5:
            results = BatterySearch.NearestNetwork(houseList, networkList)
        if subChoice == 6:
            results = TrueRandom.RandomConnect(houseList, networkList)

        if bestRandom is None:
            bestRandom = results

        failedImprovements, bestRandom = ScoreCheck(results, bestRandom, failedImprovements)

    print(f"Randomization Algorithm: couldn't find a better result after {iterations} attemps. Ran a total of {runCounter}. Final Score = {bestRandom[1]}")

    VisualJSON(bestRandom)

    return bestRandom

def Optimize(goodRandom, iterations, subChoice):
    """
    Runs the Sort random algorithm as many times as interations, and returns the best one. 
    """

    baseCost = goodRandom[1]
    optimizationAttempts = 0
    optimizedResult = goodRandom

    while optimizationAttempts < iterations:

        if subChoice == 1:
            results = ResultShuffle.Shuffle(goodRandom[2], goodRandom[1])
        elif subChoice == 2:
            results = ResultsSort.Sort(goodRandom[2], goodRandom[1])
        elif subChoice == 3:
            results = ResultsDynamicSort.Sort(goodrandom[2], goodrandom[1])

        optimizationAttempts, optimizedResult = ScoreCheck(results, optimizedResult, optimizationAttempts)

    VisualJSON(optimizedResult, goodRandom)

    print(f"Result Optimization: couldn't find a better result after {iterations} attempts. Final Score = {optimizedResult[1]}")

    return optimizedResult

def HillClimb(optimizedRandom, iterations, dynamic=False):
    """
    Runs the hillclimb algorithm as many times as iterations and returns the best result
    """

    optimizationAttempts = 0
    optimizedResult = optimizedRandom
    newPath = optimizedRandom[2].strip(".json") + "hillclimb.json"
    with open(newPath, "w+") as f:
        json.dump(optimizedRandom[0], f, indent=4)

    while optimizationAttempts < iterations:

        if dynamic:
            results = CornerChange.hillSort(newPath, optimizedResult[1], optimizedResult[3])
        else:
            results = CornerPositionChange.hillSort(newPath, optimizedResult[1], optimizedResult[3])

        optimizationAttempts, optimizedResult = ScoreCheck(results, optimizedResult, optimizationAttempts)

    if results[1] < optimizedRandom[1]:
        VisualJSON(optimizedResult, optimizedRandom)
        print(f"hillclimbSortv2: couldn't find a better result after {iterations} attempts. Final Score = {optimizedResult[1]}")
    else:
        print("hillclimbing did not improve the score. No visualization made.")

    
if __name__ == "__main__":

    # Sets the parameters of the function based on the input, and creates default values
    try:
        algorithmChoice = int(sys.argv[3])
    except:
        algorithmChoice = 10000

    try:
        filePrefix = sys.argv[2]
    except:
        filePrefix = "wijk1"

    try:
        iterations = int(sys.argv[1])
    except:
        iterations = 100


    main(filePrefix, algorithmChoice, iterations)




    