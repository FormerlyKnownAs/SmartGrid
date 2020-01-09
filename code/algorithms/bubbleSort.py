class House(object):
    """Het model voor het huis object."""
    
    def __init__(self, x, y, output):
        """Initializeert het huis."""

        self.coordinates = (x, y)
        self.output = output
        self.route = (None, None)
        self.battery = (None, None)
        self.cost = 0


    def bubbleSort(self, nlist):

        



        for cableLocations in range(len(nlist)-1,0,-1):
            for i in range(cableLocations):


                if nlist[i]>nlist[i+1]:
                    temp = nlist[i]
                    nlist[i] = nlist[i+1]
                    nlist[i+1] = temp

    nlist = [14,46,43,27,57,41,45,21,70]

    bubbleSort(nlist)
    print(nlist)




