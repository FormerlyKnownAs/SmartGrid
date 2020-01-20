from collections import defaultdict 
import json

# Source: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/


class Vertix():

    def __init__(self, coordinates, id, network):
        self.coordinates = coordinates
        self.id = id
        self.distances = {}
        self.network = network
    
    def __str__(self):
        return f" coordinates:{self.coordinates}, id: {self.id}, network: {self.network}\n"

def Sort(inputFile, previousScore):

    # Set variables to be measured
    totalCost = 0
    distanceList = [[] for i in range(5)]
    i = -1

    # Load JSON file
    with open(inputFile, 'r') as JSON:
        json_dict = json.load(JSON)

    # Declare the conversion lists
    newJSON = []

    houseCoordinates = [[]for i in range(5)]
    
    for network in json_dict:
        i += 1

        # Finds all houses associated with network
        for house in network["huizen"]:
            
            houseCoordinates[i].append(house["locatie"])
            
            # Hier vertix object aanmaken

    Formatting(houseCoordinates)

        

def Formatting(houseCoordinates):
    i = 0
    id = 0
    network = 1
    for network in houseCoordinates:
        i += 1 
        # print("network:", i)
        for house in network:
            coordinates  = house.strip(", ")
            Vertix(coordinates, id, network)
            id += 1
            # print(coordinates)
    print("netwerk 3:", houseCoordinates[2][0])
    
    for house in houseCoordinates[2]:
        
        id += 1
        print('id', id, house)
    print(houseCoordinates[2])


#Class to represent a graph 
class Graph: 
  
    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = [] # default dictionary  
                                # to store graph 
        
          
   
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    # A utility function to find set of an element i 
    # (uses path compression technique) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of  
        # high rank tree (Union by Rank) 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, then make one as root  
        # and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1

        


     
    def KruskalMST(self): 
  
        result =[] #This will store the resultant MST 
  
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 
  
            # Step 1:  Sort all the edges in non-decreasing  
                # order of their 
                # weight.  If we are not allowed to change the  
                # given graph, we can create a copy of graph 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
  
            # Step 2: Pick the smallest edge and increment  
                    # the index for next iteration 
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            # If including this edge does't cause cycle,  
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 
  
        # print the contents of result[] to display the built MST 
        print("Following are the edges in the constructed MST")
        for u,v,weight  in result: 
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
            print("%d -- %d == %d" % (u,v,weight)) 

if __name__ == "__main__":

    # Elke batterij heeft een bepaalde hoeveelheid huizen
    g = Graph(4) 


    # tussen elk huis de afstand moeten berekenen. en die toevoegen met .addEdge(#huis1, #huis2, #afstand)
    g.addEdge(0, 1, 10) 
    g.addEdge(0, 2, 6) 
    g.addEdge(0, 3, 5) 
    g.addEdge(1, 3, 15) 
    g.addEdge(2, 3, 4) 
    
    g.KruskalMST()
    Sort("networkresults_1.json",6570)
    
    