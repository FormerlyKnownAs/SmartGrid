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
        self.cables = {self.source :[]}
        self.cables = {1:[], 2:[], 3:[], 4:[], 5:[]}


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

    def BatteryCheck(self, batteries):
        """Checks the best battery based on distance and current capacity."""

    # https://stackoverflow.com/questions/398299/looping-in-a-spiral
        #  maak een figuratieve (0,0) positie voor het huis.
        X = self.coordinates[0]
        Y = self.coordinates[1]

        x = y = 0

        #  Search functie begint bij (0,-1)
        dx = 0
        dy = -1

        for i in range(max(X, Y)**2):
            
            # Loopt over een grid van 4 bij 4 
            if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
               
                print (x, y)
                # Objectieve positie berekenen
                ObjectiveX: abs(self.coordinates[0] - x)
                ObjectiveY: abs(self.coordinates[1] - y)
                ObjectivePosition = (X,Y)


                for i in Network.cables.keys():
                 
                    if ObjectivePosition in Network.cables[i]:
                        if Network.capacity > self.output:






                # Over de lijst van bekende kabels loopen, if (Objectieve positie) in self.cables:
                if ObjectivePosition in self.cables

                # Als het capaciteit heeft

            if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
                dx, dy = -dy, dx
            x, y = x+dx, y+dy              


        # Sets battery and route
        self.battery = batteries[shortestIndex].coordinates
        self.route = (self.coordinates[0], self.battery[1])
        self.cost = shortestDistance * 9
        battery.capacity -= self.output

        

    def __str__(self):
        return f"{self.coordinates}, {self.output}, {self.route}, {self.battery}, {self.cost}\n"

class Battery(object):
    """Het model voor de batterij."""

    def __init__(self, x, y, capacity):
        """Initializeert de batterij."""

        self.coordinates = (x, y)
        self.capacity = capacity

    def __str__(self):
        return f"Battery: {self.coordinates}"




   