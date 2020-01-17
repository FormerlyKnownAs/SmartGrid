import matplotlib.pyplot as plt 
import numpy as np 
import json

def Visualize(input):
    """ Loads JSON file, convert into dict or list-in-list format,
        visualize using pyplot """

    # Load JSON file
    with open(input, 'r') as JSON:
        json_dict = json.load(JSON)

    # Declare various lists and variables for converting
    battery_index = 0
    
    networks = {}
    houses = []
    batteries = []

    # Loop over batteries
    for battery in json_dict:

        networks[battery_index] = []

        # Save battery coordinates as strings
        batteries.append(ListFormat(battery["locatie"]))

        for house in battery["huizen"]:

            # Save house coordinates as strings 
            locatie = house["locatie"]
            houses.append(ListFormat(locatie))

            cableList = []

            for line in house["kabels"]:

                cableCoordinate = ListFormat(line)

                # Save cable
                cableList.append(cableCoordinate)
                
            # Save cable sequence in dict under network index          
            networks[battery_index].append(cableList)

        battery_index += 1


def ListFormat(string):

    outputList = []


    for element in string.split(","):

        element = element.strip("'()'")
        outputList.append(int(element))

    return outputList

    
    # Set up grid for visualization
    ticks = np.arange(0,50,1)
    plt.axis([0, 50, 0, 50])
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.title("SmartGrid")
    plt.xlabel("")
    plt.ylabel("")
    plt.grid(True, linewidth=0.3)

    # Line types for cable visualization
    lines = ['y-', 'b-', 'c-', 'm-', 'g-']
    colors = ['y^', 'b^', 'c^', 'm^', 'g^']


    # Draw cable
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



    input = input.strip(".json")
    plt.savefig(f'{input}.png')
    print("Visaualization graph added to resultaten.")
