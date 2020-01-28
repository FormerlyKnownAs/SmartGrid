"""

LineTrackRandominput.py

Tracks a line between two given points and returns a list of all 
points on that line. This version incorporates "controlled randomness", so
corners can be manually swapped.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

import random
import numpy as np

def TrackRandom(start, end, corner):
    """ Returns a list of all coordinates between two 
        given points. """

    # Define variables
    startX = start[0]
    startY = start[1]

    endX = end[0]
    endY = end[1]

    distanceX = abs(startX - endX)
    distanceY = abs(startY - endY)

    newX = startX
    newY = startY

    # distance = abs((startX - endX) + (startY - endY))

    coordinates = []

    if distanceY == 0:

        # Track along x-axis
        for i in range(distanceX + 1):

            # Move "right"
            if endX > startX:
                
                coordinates.append([newX, startY])
                newX += 1

            # Move "left"
            if endX < startX:

                coordinates.append([newX, startY])
                newX -= 1
                

    elif distanceX == 0:

        # Track along y-axis
        for i in range(distanceY + 1):

            # Move "up"
            if endY > startY:

                coordinates.append([startX, newY])
                newY += 1

            # Move "down"
            if endY < startY:

                coordinates.append([startX, newY])
                newY -= 1


    elif corner == 1:

        # Track along x-axis
        for i in range(distanceX):

            # Move "right"
            if endX > startX:
                
                coordinates.append([newX, startY])
                newX += 1

            # Move "left"
            if endX < startX:

                coordinates.append([newX, startY])
                newX -= 1

        # Track along y-axis
        for i in range(distanceY + 1):

            # Move "up"
            if endY > startY:

                coordinates.append([newX, newY])
                newY += 1

            # Move "down"
            if endY < startY:

                coordinates.append([newX, newY])
                newY -= 1

    else:

        # Track along y-axis
        for i in range(distanceY):

            # Move "up"
            if endY > startY:

                coordinates.append([startX, newY])
                newY += 1

            # Move "down"
            if endY < startY:

                coordinates.append([startX, newY])
                newY -= 1
        
        # Track along x-axis
        for i in range(distanceX + 1):

            # Move "right"
            if endX > startX:
                
                coordinates.append([newX, newY])
                newX += 1

            # Move "left"
            if endX < startX:

                coordinates.append([newX, newY])
                newX -= 1

    newCoordinates = []
    for cable in coordinates:
        newCoordinates.append((cable[0], cable[1]))

    return newCoordinates
