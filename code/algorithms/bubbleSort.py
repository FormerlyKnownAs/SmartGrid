class House(object):
    """Het model voor het huis object."""
    
    def __init__(self, x, y, output):
        """Initializeert het huis."""

        self.coordinates = (x, y)
        self.output = output
        self.route = (None, None)
        self.battery = (None, None)
        self.cost = 0


    def distanceCalculation(houses, networks):
        """Berekent de afstand tussen elke network locatie en het huidige huis."""

        for house in houses:

            self.distanceList = []
            self.locationList

            for networkPoint in networks:
                if networkPoint.capacity > house.output:
                    distance = abs(house.coordinates[0] - networkPoint.coordinates[0]) + abs(house.coordinates[0] - networkPoint.coordinates[1])
                    self.distanceList.append(distance)
        

    def bubbleSort(self):

        for cableDistance in range(len(self.distanceList)-1,0,-1):
            for i in range(cableDistance):


                if self.distanceList[i]>self.distanceList[i+1]:
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp

    nlist = [14,46,43,27,57,41,45,21,70]
    
    bubbleSort(nlist)
    print(nlist)
    networkUpdate()

    def networkUpdate(self, )




