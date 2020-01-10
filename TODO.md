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

