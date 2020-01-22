import json

def HouseReader():
    """ Returns a list of lists with all houses in a network """

    with open("testOutput.json", 'r') as JSON:
        json_dict = json.load(JSON)

    houseNetworksAll = []

    for battery in json_dict:

        houseNetwork = []

        for house in battery["huizen"]:

            coordinatesString = house["locatie"]
            houseNetwork.append(ListFormat(coordinatesString))

        houseNetworksAll.append(houseNetwork)

    return houseNetworksAll


def ListFormat(string):

    output = []
    
    for element in string.split(","):

        output.append(int(element))

    return output

if __name__ == "__main__":
    print(HouseReader())