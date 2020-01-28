"""

visualize.py

Generates a visualization of JSON results file.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

import matplotlib.pyplot as plt 
import numpy as np 
import json


def ListFormat(string):
    """ Converts coordinate strings to correct list
        format for visualization """

    outputList = []

    # Split string into seperate elements
    for element in string.split(","):
        
        # Strip of any brackets or quotes, put in list as integer
        element = element.strip("'()'")
        outputList.append(int(element))

    return outputList


def Visualize(input, underlay=False):
    """ Loads JSON file, put data in dict,
        visualize using pyplot """

    # Load JSON file
    with open(input, 'r') as JSON:
        json_dict = json.load(JSON)

    # Declare various lists and variables for converting  
    networks = {}
    houses = []
    batteries = []

    # Loop over batteries
    for i, battery in enumerate(json_dict):

        networks[i] = []

        # Format battery coordinate strings as list and append to battery list
        batteries.append(ListFormat(battery["locatie"]))

        for house in battery["huizen"]:

            # Format house coordinate strings as list and append to house list
            houses.append(ListFormat(house["locatie"]))

            cableList = []

            for line in house["kabels"]:

                # Format cable coordinate strings as list and append to 
                # cable list
                cableList.append(ListFormat(line))
                
            # Save cable sequence in dict under network index          
            networks[i].append(cableList)

    # Determine tick labels
    ax = plt.axes()
    ax.yaxis.set_minor_locator(plt.MultipleLocator(1))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(1))

    # Set up grid for visualization
    plt.title("SmartGrid")

    ticks = np.arange(0,51,5)
    labels = np.arange(0,51,5)
    plt.axis([-1, 51, -1, 51])
    plt.xticks(ticks, labels)
    plt.yticks(ticks, labels)

    # Lock graph aspect ratio to square
    plt.gca().set_aspect("equal", adjustable="box")

    # Plot grid
    plt.grid(True, which='both', linewidth=0.3)

    # Line types for cable visualization
    lines = ['y-', 'b-', 'c-', 'm-', 'g-']
    dotted = ['y:', 'b:', 'c:', 'm:', 'g:']

    # Draw dotted underlay vables
    if underlay:

        for i, network in enumerate(networks.values()):

            for cable in network:

                cableArray = np.array(cable)

                plt.plot(*cableArray.T, dotted[i % len(dotted)])

    # Draw cables
    else:

        for i, network in enumerate(networks.values()):

            for cable in network:

                # Convert line coordinates into array for visualization
                cableArray = np.array(cable)

                plt.plot(*cableArray.T, lines[i % len(lines)])

        # Draw houses
        for house in houses:

            plt.plot(house[0], house[1], 'r^')

        # Draw batteries
        for battery in batteries:

            plt.plot(battery[0], battery[1], 'bs')

        # Add visualization png to resultaten folder
        input = input.strip(".json")
        plt.savefig(f'{input}.png')
        plt.clf()
        print("Visualization graph added to resultaten.")
