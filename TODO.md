TODO list:

Grid structure. 

Fix format of output to align with assignment

Start visualization through matplotlib.


Class grid maken met volgende attributen:
self.completeroute (volledige route voor de kabel die ook functioneert als de batterij)
self.coordinates
battery coordinates. 

Ga je over de x of y as, en hoe check je welk optimaal is. 

Visualizatie via matpylab (check requirements.txt)

Potenieel een route class


OUTDATED
Matrix:

Een grid object met een opslag voor een matrix. Deze matrix is een dictionary, met een dictionary daar in. 

Grid slaat hetvolgend op, hier eerst een template.
{ KEY : { KEY : DATA } }
{ Coordinaten op grid : { Netwerk ID : Permutatie van objecten } }

Potentieel, de sleutels van de permutatie:
Leeg = 0
Kabel = 1
Kabel, huis = 2
Kabel, batterij = 3

{ (10, 5) : { 2 : 2 } }

Voor Jan 8 & 9:

Ons probleem lijkt op de travelling Salesman, zal wss literatuur over zijn voor betere resultaten. 

Randomization van lijst. 

Meerdere resultaten creeeren in een run. 

Dijkstra & Graph theory kan potentieel helpen. 

https://en.wikipedia.org/wiki/Quadtree

https://en.wikipedia.org/wiki/Binary_space_partitioning


WIJK 1
WORST SCORE:
10764

BEST SCORE:
6471

HOUSES CONNECTED:
27.339999999999996%

(boy):

maak een versie van nearestNetworkv2random die alle resultaten in een lijst zet en die meegeeft aan een algoritme dat de kabels tussen batteriejen opnieuwe spant, om de kosten to optimalizeren. 

(ben):

maak de beste versie uitleesbaar

Hillclimb versies:
Disconnect één huis naar keuze, en verbindt dit opnieuw. Blijf dit herhalen totdat de score niet meer verbeterd. 

Random optimalisatie:
Shuffle de huizen verbonden met batterijen, en stuur een beter resultaat terug. 

Heuristiek:
Laat de bocht keuze afhangen van het meeste mogelijk nieuwe connecties

SmartGrid:
minimum spanningtree (https://en.wikipedia.org/wiki/Kruskal%27s_algorithm, https://en.wikipedia.org/wiki/Minimum_spanning_tree)
Kijk naar pickle