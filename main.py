"""

De functionaliteit.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

import sys
import random as r
import json

from code.classes import house, network, csvreader
from code.algorithms import BatterySearch, bestFitNetwork, CornerChange, \
                            CornerPositionChange, HouseSearchFull, HouseSearchHybrid, \
                            NetworkSearch, ResultsDynamicSort, ResultShuffle, \
                            ResultsSort, TrueRandom
from code.visualization import visualize

def main(iterations, filePrefix, Randomizer, Optimizer, Finisher):
    """ Chooses the file, function and repetition, and sends the output to 
        the visualizer. Takes a number of interations, a prefix as arguments, and
        the three choices of algorithm. """

    # Runs the chosen algorithms
    if Randomizer != 0:
        randomizedResult = Random(filePrefix, iterations, Randomizer)
        if Optimizer != 0:
            optimizedResult = Optimize(randomizedResult, iterations * 2, Optimizer)
            if Finisher != 0 and optimizedResult[1] is True:
                finalResult = Finalize(optimizedResult[0], iterations * 4, Finisher)
    else:
        print("Please select an algorithm.")

def readinInfo(filePrefix):
    """ Reads in the csv files for the neighborhoods. Takes a fileprefix as an
        argument. """
    houseList = csvreader.LoadHouses(f"data/{filePrefix}_huizen.csv")
    networkList = csvreader.LoadNetwork(f"data/{filePrefix}_batterijen.csv")

    return houseList, networkList


def ScoreCheck(newResults, previousResults, failedImprovements):
    """ Compares scores, increments counter and returns the better result. Takes
        two sets of results and a number of failed improvements as argument. """

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

def VisualJSON(result):
    """ Creates a JSON file and visualizes the result, based on the result given
        as input. """

    # Writes the JSON file
    with open(result[2], "w+") as f:
        json.dump(result[0], f, indent=4)

    visualize.Visualize(result[2])

def Random(filePrefix, iterations, subChoice):
    """ Runs a randomizer algorithm as many times as iteration. Takes a
        file prefix, a number of iterations and a choice of algorithm as 
        argument. """

    # Sets the counters to correctly iterate over results
    runCounter = 0
    failedImprovements = 0
    bestScore = 1000
    bestRandom = None

    # Runs through results, disregarding invalid solutions
    while failedImprovements < iterations:

        runCounter += 1
        houseList, networkList = readinInfo(filePrefix)
        
        if subChoice == 1:
            results = TrueRandom.RandomConnect(houseList, networkList)    
        if subChoice == 2:
            results = BatterySearch.NearestNetwork(houseList, networkList)    
        if subChoice == 3:
            results = bestFitNetwork.BestFit(houseList, networkList)  
        if subChoice == 4:
            results = HouseSearchHybrid.NearestHouse(houseList, networkList)
        if subChoice == 5:
            results = HouseSearchFull.NearestHouse(houseList, networkList)
        if subChoice >= 6:
            results = NetworkSearch.NearestNetwork(houseList, networkList)

        # Makes sure the first result is set
        if bestRandom is None:
            bestRandom = results

        failedImprovements, bestRandom = ScoreCheck(results, bestRandom, failedImprovements)

    print("Randomization Algorithm: couldn't find a better result after" \
        f"{iterations} attemps. Ran a total of {runCounter}. Final Score" \
        f"= {bestRandom[1]}")

    VisualJSON(bestRandom)

    return bestRandom

def Optimize(goodRandom, iterations, subChoice):
    """ Runs an optimzer algorithm as many times as iterations. Takes 
        a previous reuslt, a number of iterations and a choice of algorithm
        as argument. """

    # Sets the base to improve over
    baseCost = goodRandom[1]
    optimizationAttempts = 0
    optimizedResult = goodRandom

    # Iterates through results and sets improvements as new standard
    while optimizationAttempts < iterations:

        if subChoice == 1:
            results = ResultShuffle.Shuffle(goodRandom[2], goodRandom[1])
        elif subChoice == 2:
            results = ResultsSort.Sort(goodRandom[2], goodRandom[1])
        elif subChoice >= 3:
            results = ResultsDynamicSort.Sort(goodRandom[2], goodRandom[1])

        optimizationAttempts, optimizedResult = ScoreCheck(results, optimizedResult, optimizationAttempts)

    wasOptimized = False
    if optimizedResult[1] < goodRandom[1]: 
        print("Result Optimization: couldn't find a better result after" \
            f"{iterations} attempts. Final Score = {optimizedResult[1]}")

        VisualJSON(optimizedResult)
        wasOptimized = True
    else:
        print("Optimizing did not improve the score. No visualization " \
            f"made. Score remains {optimizedResult[1]}")

    return optimizedResult, wasOptimized

def Finalize(optimizedRandom, iterations, subChoice):
    """ Runs a finalizer algorithm as many times as iterations. Takes an 
        optimized result, a number of iterations and a choice of
        algorithm as argument. """
    
    # Sets the base for improvement
    optimizationAttempts = 0
    optimizedResult = optimizedRandom
    newPath = optimizedRandom[2].strip(".json") + "hillclimb.json"

    # Creates dummy JSON to update throughout process
    with open(newPath, "w+") as f:
        json.dump(optimizedRandom[0], f, indent=4)

    # Iterates over results and sets improvements as new standard
    while optimizationAttempts < iterations:

        if subChoice == 1:
            results = CornerChange.hillSort(newPath, optimizedResult[2], optimizedResult[1])
        elif subChoice >= 2:
            results = CornerPositionChange.hillSort(newPath, optimizedResult[2], optimizedResult[1])

        optimizationAttempts, optimizedResult = ScoreCheck(results, optimizedResult, optimizationAttempts)

    # Visualizes results and updates user about final status.
    if results[1] < optimizedRandom[1]:
        print(f"Finalizing: couldn't find a better result after {iterations}" \
            f" attempts. Final Score = {optimizedResult[1]}")

        VisualJSON(optimizedResult)
    else:
        print(f"Finalizing did not improve the score. No visualization made. " \
             f"Score remains = {optimizedResult[1]}")

if __name__ == "__main__":

    # Sets the parameters of the function based on the input, and creates default values
    try:
        iterations = int(sys.argv[1])
    except:
        iterations = 100
    
    try:
        filePrefix = sys.argv[2]
    except:
        filePrefix = "wijk1"
    
    try:
        randomizer = int(sys.argv[3])
    except:
        randomizer = 1000

    try:
        optimizer = int(sys.argv[4])
    except:
        optimizer = 1000

    try:
        finalizer = int(sys.argv[5])
    except:
        finalizer = 1000

    main(iterations, filePrefix, randomizer, optimizer, finalizer)




    