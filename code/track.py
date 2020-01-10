def track(start, end):
    """ Returns a list of all coordinates between two given points, except for the last one"""

    # Define variables
    startX = start[0]
    startY = start[1]

    endX = end[0]
    endY = end[1]

    distanceX = abs(startX - endX)
    distanceY = abs(startY - endY)

    # distance = abs((startX - endX) + (startY - endY))

    coordinates = []
    
    # Track along x-axis
    for i in range(distanceX):

        # Move "right"
        if endX > startX:
            
            coordinates.append((startX + i, startY))

        # Move "left"
        if endX < startX:

            coordinates.append((startX - i, startY))

    # Track along y-axis
    for i in range(distanceY):

        # Move "up"
        if endY > startY:

            coordinates.append((startX + distanceX, startY + i))

        # Move "down"
        if endY < startY:

            coordinates.append((startX + distanceX, startY - i))

    return coordinates


house = (2, 7)
network = (10, 5)


path = track(house, network)
print(path)