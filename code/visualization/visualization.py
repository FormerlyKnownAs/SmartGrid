import matplotlib.pyplot as plt 
import numpy as np 
import json


with open("resultaten/networkresults_1.json", 'r') as JSON:
    json_dict = json.load(JSON)


batteriesStrings = []
housesStrings = []
cables = {}
house_index = 0
houses = []
batteries = []




for battery in json_dict:

    batteriesStrings.append(battery["locatie"])

    for house in battery["huizen"]:

        locatie = house["locatie"]
        housesStrings.append(locatie)
        cableList = []

        for line in house["kabels"]:

            cableCoordinate = []

            for element in line.split(","):

                strippedElement = element.strip("'()'")
                cableCoordinate.append(int(strippedElement))
            
            cableList.append(cableCoordinate)
            
        cables[house_index] = cableList
        house_index += 1

# Convert house coordinates to list-in-list format

for house in housesStrings:

    houseCoordinate = []

    for element in house.split(","):

        houseCoordinate.append(int(element))

    houses.append(houseCoordinate)

# Convert battery coordinates to list-in-list format

for battery in batteriesStrings:

    batteryCoordinate = []

    for element in battery.split(","):

        batteryCoordinate.append(int(element))

    batteries.append(batteryCoordinate)

                

ticks = np.arange(0,50,1)
plt.axis([0, 50, 0, 50])
plt.xticks(ticks)
plt.yticks(ticks)
plt.title("SmartGrid")
plt.xlabel("")
plt.ylabel("")
plt.grid(True, linewidth=0.3)
lines = ['r:', 'b:', 'c:', 'm:']



for i, cable in enumerate(cables.values()):

    cablearray = np.array(cable)
    plt.plot(*cablearray.T, lines[i % 3])

for house in houses:

    plt.plot(house[0], house[1], 'r^')

for battery in batteries:

    plt.plot(battery[0], battery[1], 'bs')

plt.show()





