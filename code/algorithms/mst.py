"""
Proof of concept for Kruskal's minimum spanning tree algorithm

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

from collections import defaultdict 
import json

# Source: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/


class Vertix():

    def __init__(self, coordinates, id, network):
        self.coordinates = coordinates
        self.id = id
        self.network = network
    
    def __str__(self):
        return f"Vertix id: {self.id}, coordinates: {self.coordinates}, network: {self.network}"


def ListFormat(string):

    outputList = []

    for element in string.split(","):

        element = element.strip("'()'")
        outputList.append(int(element))

    return outputList


def Load(input):
    """ Loads JSON file, convert into dict or list-in-list format,
        visualize using pyplot """

    # Load JSON file
    with open(input, 'r') as JSON:
        json_dict = json.load(JSON)

    # Declare various lists and variables for converting  
    networks = {}
    vertixes = []

    # Loop over batteries
    for i, battery in enumerate(json_dict):

        networks[i] = []

        # Format battery coordinate strings as list and append to battery list
        networks[i].append(ListFormat(battery["locatie"]))

        for j, house in enumerate(battery["huizen"]):

            # Format house coordinate strings as list and append to house list
            networks[i].append(ListFormat(house["locatie"]))

            v = Vertix(ListFormat(house["locatie"]), j, i)
            vertixes.append(v)

    

    return vertixes


def DistanceCalculator(network):

    networkDistances = []

    for i, node in enumerate(network):

        for j, nodeTo in enumerate(network):
            fromToDistance = []

            distance = abs(node[0] - nodeTo[0]) + abs(node[1] - nodeTo[1])
            fromToDistance = [i, j, distance]

            networkDistances.append(fromToDistance)

    return networkDistances


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
  
    # The main function to construct MST using Kruskal's  
        # algorithm 
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
        print ("Following are the edges in the constructed MST")
        for u,v,weight  in result: 
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
            print ("%d, %d" % (u, v)) 
  

if __name__ == "__main__":

    

    vertixes, networks = Load("networkresults_1.json")

    for vertix in vertixes:
        print(vertix)

    for i, network in enumerate(networks):

        for vertix in vertixes in vertix.network == i:

            




    networkNodeList = []




    # for network in networks.values():

    #     nodes = DistanceCalculator(network)

    #     networkNodeList.append(nodes)

    # g = Graph(31)
  
    # for i, network in enumerate(networkNodeList):

        

    #     for node in networkNodeList[i]:

    #         if node[0] != node[1]:
    #             g.addEdge(node[0], node[1], node[2])

    #     g.KruskalMST()
    #     print("\n")

    