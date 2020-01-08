from models import Battery, House
import csv

def ReadCSV(filePath):

    # Makes list to return to be filled with csv data
    emptyList = []
    
    with open(filePath, "r") as f:

        # Skips header
        csvreader = csv.reader(f)
        next(csvreader, None)

        # Reads the lines
        for line in f:
            
            # Makes an empty list to append data to
            emptyData = []

            # Splits the data per line
            for element in line.split(","):

                # Reads out numbers and stores them as floats
                element = element.strip('"[]"')
                emptyData.append(float(element))

            # Checks object kind and makes correct object

            if "huizen" in filePath:
                print("current csv object is a house")
                newObject = House(emptyData[0], emptyData[1], emptyData[2])
            else:
                newObject = Battery(emptyData[0], emptyData[1], emptyData[2])

            emptyList.append(newObject)
    
    return emptyList

if __name__ == "__main__":
    listOfHouses  = ReadCSV("data/testWijk_huizen.csv")
    listOfBatteries = ReadCSV("data/testWijk_batterijen.csv")
    
    print("\nHuizen:")
    for house in listOfHouses:
        print(house)

    print("\nbatteries:")
    for battery in listOfBatteries:
        print(battery)
