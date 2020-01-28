"""

mst.py

Concept implementation of a Kruskal MST algorithm. Finally decided it would be 
suboptimal for our problem; also could't correctly fit the output in our existing
structure.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

import json

def ListFormat(string):
    """ Converts a coordinate string to a list. Takes coordinates as a string
    as argument. """
    outputList = []

    # Loop over elements in string
    for element in string.split(","):

        # Strip coordinates of brackets and quotes, turn into int
        element = element.strip("'()'")
        outputList.append(int(element))

    return outputList


def Load(input):
    """ Loads JSON file, convert into dict or list-in-list format,
        visualize using pyplot. """

    # Load JSON file
    with open(input, 'r') as JSON:
        json_dict = json.load(JSON)

    # Declare various lists and variables for converting  
    networks = {}

    # Loop over batteries
    for i, battery in enumerate(json_dict):

        networks[i] = []

        # Format battery coordinate strings as list and append to battery list
        networks[i].append(ListFormat(battery["locatie"]))

        for j, house in enumerate(battery["huizen"]):

            # Format house coordinate strings as list and append to house list
            networks[i].append(ListFormat(house["locatie"]))


    return networks


def DistanceCalculator(network):
    """ Calculates distances between all nodes in a given
        network and outputs them into a correct format for the
        Kruskal function. Input is network list. """

    networkDistances = []

    # Loop over nodes in networks
    for i, node in enumerate(network):

        # For every node, loop over all nodes
        for j, nodeTo in enumerate(network):

            # Skip if node connects to self
            if i != j:

                fromToDistance = []

                # Calculate distance (weight) and format
                distance = abs(node[0] - nodeTo[0]) + abs(node[1] - nodeTo[1])
                fromToDistance = [i, j, distance]

                networkDistances.append(fromToDistance)

    return networkDistances


class Graph: 
    """
    Source: 
    https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
    
    """

    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
          
    # Function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    # A utility function to find set of an element i 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that unites two sets of x and y 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
        # Attach smaller rank tree under root of high rank tree 
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
        # If ranks are same, make one as root and increment its rank by one 
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
    
    def KruskalMST(self): 
        """ Main function to construct Kruskal MST algorithm. """
  
        result =[] 
  
        i = 0 
        e = 0 
  
        # Sort all the edges in non-decreasing order of their weight
        self.graph = sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
  
            # Pick the smallest edge and increment index
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            # If no cycle, include edge in result and increment
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
  
        # print results to display the MST 
        for u,v,weight  in result: 
            print (f"from node {u} to node {v}, with weight {weight}.")
  

def MST(inputFile):
    """ Concept version, will print all optimal connections in network,
        calculated by Kruskal's MST. inputFile is JSON file. """

    # Load networks from JSON file
    networks = Load(inputFile)

    networkNodesDict = {}
    networkLengths = []

    # Iterate over networks
    for i, network in enumerate(networks.values()):

        # Calculate distances between all nodes in network
        nodes = DistanceCalculator(network)

        # Put in dict
        networkNodesDict[i] = nodes

        # Save number of nodes for input in Kruskal algorithm
        networkLengths.append(len(network))

    # Iterate over networks (nodes)
    for i, network in enumerate(networkNodesDict.values()):

        print(f"CONNECTIONS FOR NETWORK {i}:\n")

        # Prime Graph class for correct numer of nodes
        g = Graph(networkLengths[i])
        
        # Iterate over nodes
        for node in network:
    
            # Add edges in format: node, node, weight
            g.addEdge(node[0], node[1], node[2])

        # Generate MST
        g.KruskalMST()
        print("\n")

    