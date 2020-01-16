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
    batteriesStrings = []
    battery_index = 0

    housesStrings = []
    
    networks = {}
    houses = []
    batteries = []

    # Loop over batteries
    for battery in json_dict:

        networks[battery_index] = []

        # Save battery coordinates as strings
        batteriesStrings.append(battery["locatie"])

        for house in battery["huizen"]:

            # Save house coordinates as strings 
            locatie = house["locatie"]
            housesStrings.append(locatie)
            cableList = []

            for line in house["kabels"]:

                cableCoordinate = []

                for element in line.split(","):

                    # Save and convert cable segment coordinates
                    strippedElement = element.strip("'()'")
                    cableCoordinate.append(int(strippedElement))
                
                # Save cable
                cableList.append(cableCoordinate)
                
            # Save cable sequence in dict under network index          
            networks[battery_index].append(cableList)

        battery_index += 1


    # Convert house coordinates to list-in-list format
    for house in housesStrings:

        houseCoordinate = []

        for element in house.split(","):

            # Convert house coordinates
            houseCoordinate.append(int(element))

        houses.append(houseCoordinate)

    # Convert battery coordinates to list-in-list format
    for battery in batteriesStrings:

        batteryCoordinate = []

        for element in battery.split(","):

            # Convert battery coordinates
            batteryCoordinate.append(int(element))

        batteries.append(batteryCoordinate)

    
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
    plt.clf()
    print("Visaualization graph added to resultaten.")
