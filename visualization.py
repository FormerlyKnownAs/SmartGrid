import matplotlib.pyplot as plt 
import numpy as np 
import csv

def load():

    allNetworks = []
    connection = []
    

    with open(f"../SmartGrid/paths.txt", "r") as f:

        next(f)

        for line in f:
            allCoordinates = line.split(',')
            networks.append(allCoordinates)



    print(networks)

            




def main():

    # with open(f"paths.txt", "r") as f:
        


    # x = np.arange(1,5)
    # y = x**3


    # plt.plot([1,2,3,4],[1,4,9,16],'go-', x, y,'r^-')
    # plt.axis([0, 6, 0, 20])
    # plt.title("First plot")
    # plt.xlabel("Xlabel")
    # plt.ylabel("Ylabel")
    # plt.grid()
    # plt.show()


    x = [2,2,1]
    y = [5,7,7]
    x2 = [5,9,9]
    y2 = [2,2,4]
    x3 = [6,6,9]
    y3 = [1,5,5]
    x4 = [5,6,6]
    y4 = [2,2,8]

    xlist = [x, x2, x3, x4]
    ylist = [y, y2, y3, y4]
    args = ['go-', 'k^-', 'bo-']
    lines = ['r--', 'b.-', 'c:', 'm-']


    for i in range(4):

        # Lines
        plt.plot(xlist[i], ylist[i], lines[i])
        
        # Houses
        plt.plot(xlist[i][0], ylist[i][0], 'bs')

        # Batteries
        plt.plot(xlist[i][2], ylist[i][2], 'r^')


    # for i in range(3):
    #     plt.plot(xlist[i], ylist[i], args[i])

    # plt.plot(x, y, 'go-')
    # plt.plot(x2, y2, 'k^-')
    # plt.plot(x3, y3, 'bo-')
    

    plt.axis([0, 10, 0, 10])
    plt.title("First plot")
    plt.xlabel("Xlabel")
    plt.ylabel("Ylabel")
    plt.grid()
    plt.show()



    """https://stackoverflow.com/questions/35363444/plotting-lines-connecting-points"""

    def connectpoints(x,y,p1,p2):
        x1, x2 = x[p1], x[p2]
        y1, y2 = y[p1], y[p2]
        plt.plot([x1,x2],[y1,y2],'k-')


load()