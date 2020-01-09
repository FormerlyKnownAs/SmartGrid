"""
06-01-2020


De modellen voor de SmartGrid assignment.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""


class Network(object):
    """The model for a cable network."""

    def __init__(self, x, y, capacity):
        """Initializes the source location and capacity of the battery."""

        self.capacity = capacity
        self.source = (x, y)
        
        # Verandert naar een dictionarry van lijsten
        
        


        sourceCable = (x, y)
        self.cables.append(sourceCable)

    def __str__(self):
        return f"{self.capacity}, {self.source}, cables: {self.cables}"

class House(object):
    """Het model voor het huis object."""
    
    def __init__(self, x, y, output):
        """Initializeert het huis."""

        self.coordinates = (x, y)
        self.output = output
        self.route = (None, None)
        self.battery = (None, None)
        self.cost = 0

    def BatteryCheck(self, cablesDict,batteryCapacity):
        """Checks the best battery based on distance and current capacity."""

    # https://stackoverflow.com/questions/398299/looping-in-a-spiral
        # specificeert de groote van search grid.
        X = 5
        Y = 5

        x = y = 0

        #  Search functie begint bij (0,-1)
        dx = 0
        dy = -1

        for i in range(max(X, Y)**2):
            
             
            if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
               
                print (x, y)
                # Objectieve positie berekenen
                ObjectiveX = self.coordinates[0] + x
                ObjectiveY = self.coordinates[1] + y
                ObjectivePosition = (ObjectiveX, ObjectiveY)


                for i in cablesDict.keys():
                 
                    if ObjectivePosition in cablesDict[i]:

                        if batteryCapacity[i] > self.output:

                            network = i
                            # Hoeveel x posities verplaatst moeten worden
                            xRoute = self.coordinates[0] - ObjectivePosition[0]
                            yRoute = self.coordinates[1] - ObjectivePosition[1]

                            #  If x position of network location is higher than the position of the house
                            if ObjectivePosition[0] > self.coordinates[0]:
                                for j in range(xRoute):
                                    cablePosition = (self.coordinates[0] + j)
                                    cablesDict[i].add((cablePosition, self.coordinates[1]))
                                    adjustedX = self.coordinates[0] + xRoute
                                    # cablePosition en je pakt self.coordinates

                            #  If x position of network location is lower than the position of the house
                            if ObjectivePosition[0] < self.coordinates[0]:
                                for j in range(xRoute):
                                    cablePosition = (self.coordinates[0] - j)
                                    cablesDict[i].add((cablePostion, self.coordinates[1]))
                                    adjustedX = self.coordinates[0] - xRoute

                            #  If y position of network location is higher than the position of the house
                            if ObjectivePosition[1] > self.coordinates[1]:
                                for j in range(yRoute):
                                    cablePosition = (self.coordinates[1] + j)
                                    cablesDict[i].add((adjustedX, cablePosition))

                            #  If y position of network is lower than the position of the house
                            if ObjectivePosition[1] < self.coordinates[1]:
                                for j in range(yRoute):
                                    cablePosition = (self.coordinates[1] - j)
                                    cablesDict[i].add((adjustedX, cablePosition)
            
            if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
                dx, dy = -dy, dx
            x, y = x+dx, y+dy              


    # Adjusts network capacity
    batteryCapacity[network] -= self.output
    print(cablesDict)

        

    def __str__(self):
        return f"{self.coordinates}, {self.output}, {self.route}, {self.cost}\n"

class Battery(object):
    """Het model voor de batterij."""

    def __init__(self, x, y, capacity):
        """Initializeert de batterij."""

        self.coordinates = (x, y)
        self.capacity = capacity

    def __str__(self):
        return f"Battery: {self.coordinates}"




   
