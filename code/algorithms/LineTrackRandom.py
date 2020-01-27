import random
import numpy as np

def TrackRandom(start, end):
    """ Returns a list of all coordinates 
        between two given points. """

    # Define variables
    startX = start[0]
    startY = start[1]

    endX = end[0]
    endY = end[1]

    distanceX = abs(startX - endX)
    distanceY = abs(startY - endY)

    newX = startX
    newY = startY

    coordinates = []

    # Execute if line moves on x-axis only
    if distanceY == 0:

        # Track along x-axis, distance + 1 for final segment
        for i in range(distanceX + 1):

            # Move "right"
            if endX > startX:
                
                coordinates.append([newX, startY])
                newX += 1

            # Move "left"
            if endX < startX:

                coordinates.append([newX, startY])
                newX -= 1
                
    # Execute if line moves on y-axis only
    elif distanceX == 0:

        # Track along y-axis, distance + 1 for final segment
        for i in range(distanceY + 1):

            # Move "up"
            if endY > startY:

                coordinates.append([startX, newY])
                newY += 1

            # Move "down"
            if endY < startY:

                coordinates.append([startX, newY])
                newY -= 1

    # Random, move on x-axis first
    elif np.random.randint(2) == 1:

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

        # Track along y-axis, distance + 1 for final segment
        for i in range(distanceY + 1):

            # Move "up"
            if endY > startY:

                coordinates.append([newX, newY])
                newY += 1

            # Move "down"
            if endY < startY:

                coordinates.append([newX, newY])
                newY -= 1

    # Random, move on y-axis first
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
        
        # Track along x-axis, distance + 1 for final segment
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
