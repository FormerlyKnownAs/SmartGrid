"""

mst.py
21-01-2020

Concept implementation of a Kruskal MST algorithm. Finally decided it would be 
suboptimal for our problem; also could't correctly fit the output in our existing
structure.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap

"""

import json

class Vertix():
    """ Concept Vertix class, to be able to translate node ID's back into
        house objects """

    def __init__(self, coordinates, id, network):
        self.coordinates = coordinates
        self.id = id
        self.network = network
    
    def __str__(self):
        return f"Vertix id: {self.id}, coordinates: {self.coordinates}, network: {self.network}"


def ListFormat(string):
    """ Mold string coordinates into correct list format for
        further calculation. """

    outputList = []

    # Loop over elements in string
    for element in string.split(","):

        # Strip coordinates of brackets and quotes, turn into int
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
        Kruskal function. """

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
    Source: https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
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
        """ Main function to construct Kruskal MST algorithm.
        """
  
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
  

def MST(input)

    networks = Load("networkresults_5.json")

    networkNodesDict = {}
    networkLengths = []

    for i, network in enumerate(networks.values()):

        nodes = DistanceCalculator(network)

        networkNodesDict[i] = nodes

        networkLengths.append(len(network))

  
    for i, network in enumerate(networkNodesDict.values()):

        print(f"CONNECTIONS FOR NETWORK {i}:\n")
        g = Graph(networkLengths[i])
        
        for node in network:
    
            g.addEdge(node[0], node[1], node[2])

        g.KruskalMST()
        print("\n")

    