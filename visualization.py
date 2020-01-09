import matplotlib.pyplot as plt 
import numpy as np 
import csv

def load():
    
    allCoordinates = []

    with open(f"paths.txt", "r") as f:

        next(f)

        for line in f:

            connection = []
            connectionCoordinates = []

            for element in line.split(','):
                    
                element = element.strip('" () "')
                connection.append(float(element))
                
            connectionCoordinates = [connection[0], connection[1], connection[3], connection[4], connection[5], connection[6]]
            allCoordinates.append(connectionCoordinates)

    return allCoordinates


def visualize():

    allCoordinates = load()

    xlist = []
    ylist = []
    lines = ['r:', 'b-.', 'c:', 'm-.']

    for connection in allCoordinates:

        x = [connection[0], connection[2], connection[4]]
        xlist.append(x)

        y = [connection[1], connection[3], connection[5]]
        ylist.append(y)

    for i in range(len(allCoordinates)):

        # Lines
        plt.plot(xlist[i], ylist[i], lines[i % 3])
        
        # Batteries
        plt.plot(xlist[i][0], ylist[i][0], 'r^')

        # Houses
        plt.plot(xlist[i][2], ylist[i][2], 'bs')

    ticks = np.arange(0,50,1)
    plt.axis([0, 50, 0, 50])
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.title("SmartGrid")
    plt.xlabel("")
    plt.ylabel("")
    plt.grid(True, linewidth=1)
    plt.show()


def main():


    """
    https://stackoverflow.com/questions/35363444/plotting-lines-connecting-points

    def connectpoints(x,y,p1,p2):
        x1, x2 = x[p1], x[p2]
        y1, y2 = y[p1], y[p2]
        plt.plot([x1,x2],[y1,y2],'k-')
    """

visualize()