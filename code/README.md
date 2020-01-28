# SmartGrid
The SmartGrid assignment repository for the group 'The Group Formerly Known as 'The Prince Statement' '

Ben Groot, Boy Stekelbos, Momo Schaap

De code is verdeeld in drie mappen. In algorithms staan de algorithmes en heuristieken die gebruikt worden, en hulpfuncties die de heuristieken nodig heeft om te kunnen functioneren. 

In de map classes staat de datastructuur en de csvreader. 

In de map visualization staat het bestand om de outputs te kunnen functioneren.

## Algorithms:

#### BatterySearch:
Randomizer: Leest willekeurig de huizen in, gaat daarna op basis van afstand en beschikbaardheid connecties maken met batterijen

#### bestFitNetwork.py:
Randomizer: Leest willekeurig de huizen in en verbindt de huizen met batterijen gebaseerd op grootste beschikbare capaciteit.

#### CornerChange.py:
Finalizer: Leest een geoptimalizeerde output in en verandert één bocht-aanlegging in de data, en legt vervolgens gebaseerd op afstand tot het netwerk opnieuw kabels aan. 

#### CornerPositionChange.py:
Finalizer: Identiek aan CornerChange.py, maar kan ook mogelijk ook de aanleg volgorde van een netwerk aanpassen, door de inleesvolgorde van de huizen aan te passen en een huis een klein aantal plaatsen te veranderen.

#### HouseSearchFull.py:
Randomizer: Leest willekeurige de netwerken in en loopt er door heen. Voor elk netwerk vindt het het dichtsbijzijnde huis en verbindt het zolang de capaciteit dat acht. 

#### HouseSearchHybrid.py:
Randomizer: Identiek aan HouseSearchFull.py, maar stopt de aanpak vlak voor het einde en verbindt de laatste huizen gebaseerd op volgorde van de huizen in de lijst, in plaats van afstand tot netwerk

#### linetrack.py:
Ondersteunend: Maakt en slaat een lijn op van begin punt tot eind punt waar Manhattan distance gebruikt wordt.

#### LineTrackRandom.py:
Ondersteunend: Maakt en slaat een lijn op van begin punt tot eind punt waar de hoek die de lijn neemt willekeurig is terwijl deze altijd vast staat bij de normale lineTrack.

#### LineTrackRandomInput:
Ondersteunend: Doet hetzelfde als LineTrackRandom maar de manier hoe de hoek genomen wordt, wordt besloten door de gebruiker van het programma.

#### lowerBoundCalculator.py:
Ondersteunend: Berekent een mogelijke lowerbound van een wijk gebaseerd op de afstand tussen huizen en batterijen, neemt de capaciteit van de batterijen niet in consideratie, waardoor dit alleen de theoretische lowerbound is.

#### mst.py:
Ondersteunend: Kan de configuratie van verbindingen tussen batterijen en huizen inlezen en verbindt ze optimaal via een Kruskal minimal spanning tree algorithme, en geeft deze nodes terug als return value. Dit bestand kan resultaten produceren en laat een mogelijke aanpak zien, maar wordt niet daadwerkelijk gebruikt. Functioneerd als proof of concept.

#### NetworkSearch.py:
Randomizer: De volgorde van het inlezen van de huizen is willekeurig, vervolgens maakt het verbindingen tussen huizen en netwerken, gebaseerd op de dichtsbijzijnde beschikbare kabel.

#### ResultsDynamicSort.py:
Optimizer: Houdt de configuratie die gemaakt is tussen welke huizen verbonden zijn met welke batterijen. Vervolgens verwijdert het de kabels en maakt nieuwe kabels gebaseerd op afstand tussen een huis en netwerk. Verbindt altijd het dichtsbijzijnde huis. 

#### ResultsShuffle.py:
Optimizer: Doet hetzelfde als ResultsDynamicSort behalve dat de inleesvolgorde van huizen willekeurig is, in plaats van op afstand.

#### ResultsSort.py:
Optimizer: Houdt de configuratie die gemaakt is tussen welke huizen verbonden zijn met welke batterijen. Vervolgens haalt het deze kabels weg. Gaat over elk netwerk heen en sorteert de huizen op basis van afstand en maakt nieuwe kabels aan.

#### TrueRandom.py:
Randomizer: Leest de huizen in op een willekeurige volgorde en verbindt ze aan een willekeurige batterij.