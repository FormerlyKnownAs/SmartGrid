import matplotlib.pyplot as plt 
import numpy as np 
import json


def ListFormat(string):
    """ Converts coordinate strings to correct list-in-list
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

                # Format cable coordinate strings as list and append to cable list
                cableList.append(ListFormat(line))
                
            # Save cable sequence in dict under network index          
            networks[i].append(cableList)

    
    # Set up grid for visualization
    ticks = np.arange(0,50,1)
    plt.axis([0, 50, 0, 50])
    plt.xticks(ticks, labels=ticks)
    plt.yticks(ticks, labels=ticks)
    plt.title("SmartGrid")
    plt.xlabel("")
    plt.ylabel("")

    plt.grid(True, linewidth=0.3)

    # Line types for cable visualization
    lines = ['y-', 'b-', 'c-', 'm-', 'g-']
    dotted = ['y:', 'b:', 'c:', 'm:', 'g:']

    # Draw cable
    if underlay:

        for i, network in enumerate(networks.values()):

            for cable in network:

                cablearray = np.array(cable)

                plt.plot(*cablearray.T, dotted[i % len(dotted)])

    else:

        for i, network in enumerate(networks.values()):

            for cable in network:

                # Convert line coordinates into array for visualization
                cablearray = np.array(cable)

                plt.plot(*cablearray.T, lines[i % len(lines)])

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
        print("Visaualization graph added to resultaten.")
