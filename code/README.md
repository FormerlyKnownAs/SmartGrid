# SmartGrid
The SmartGrid assignment repository for the group 'The Group Formerly Known as 'The Prince Statement' '

Ben Groot, Boy Stekelbos, Momo Schaap

De code is verdeeld in drie mappen. In algorithms staan de algorithmes en heuristieken die gebruikt worden, en hulpfuncties die de heuristieken nodig heeft om te kunnen functioneren. 

In de map classes staat de datastructuur en de csvreader. 

In de map visualization staat het bestand om de outputs te kunnen functioneren.

## Algorithms:

#### BatterySearch:
Leest willekeurig de huizen in, gaat daarna op basis van afstand  en beschikbaardheid connecties maken met batterijen

#### bestFitNetwork.py:
Algoritme dat huizen verbindt op aparte netwerken aan de batterijen waar die het beste in passen qua capaciteit.

#### CornerChange.py:
Neemt een redelijk geoptimaliseerde oplossing en vervolgens verandert het de hoek die de kabels nemen om de connectiepunt van het netwerk te bereiken.

#### CornerPositionChange.py:
Neemt een redelijk geoptimaliseerde oplossing en vervolgens verandert het de hoek die de kabels nemen om de connectiepunt van het netwerk te bereiken. Ook verandert het de inleesvolgorde van de huizen met gerugeleerde mate.

#### HouseSearchFull.py:
Werkt uit een battery first approach waar het van nature clusters vormt met huizen. Vanaf de batterij zoekt het de dichtsbijzijnde huis en maakt daar een connectie mee vervolgens zoekt het naar de dichstbijzijdnste huis vanaf dat punt en maakt weer een connectie

#### HouseSearchHybrid.py:
Doet hezelfde als de HouseSearchFull maar sinds er geen viable solutions uit deze versie kwam, zorgt deze versie er voor dat de laatste 10 huizen willekeurig verbonden raken. Dit vermeidt het probleem van dat er geen oplossingen gevonden worden.

#### linetrack.py:
Maakt en slaat een lijn op van begin punt tot eind punt waar Manhattan distance gebruikt wordt.

#### LineTrackRandom.py:
Maakt en slaat een lijn op van begin punt tot eind punt waar de hoek die de lijn neemt willekeurig is terwijl deze altijd vast staat bij de normale lineTrack.

#### LineTrackRandomInput:
Doet hetzelfde als LineTrackRandom maar de manier hoe de hoek genomen wordt, wordt besloten door de gebruiker van het programma.

#### lowerBoundCalculator.py:
Berekent de lower bound van een wijk gebaseerd op de afstand tussen huizen en batterijen, neemt de capaciteit van de batterijen niet in cosideratie, waardoor dit alleen de theoretische lowerbound is.

#### mst.py(conceptueel onverenigbaar):
Niet volledig afgemaatk, maar aangepast om de configuratie tussen huizen en batterijen te onthouden en te accepteren in het programma. Deze als nodes in het programma te stoppen om vervolgens de minimum spanning tree te vinden.

#### NetworkSearch.py:
Genereert de initiele configuratie waar andere algoritmen uiteindelijk mee verder werken. De volgorde van het inlezen van de huizen is willekeurig, vervolgens maakt het verbindingen tussen huizen en batterijen op basis van afstand. dit generereert een netwerk van kabels die vervolgens ook meegenomen worden in de afstandsberekening.

#### ResultsDynamicSort.py:
Houdt de configuratie die gemaakt is tussen welke huizen verbonden zijn met welke batterijen. Vervolgens verwijdert het de kabels en maakt nieuwe kabels aan gebaseerd op de afstand tussen het huis en de dichstbijzijnde netwerk punt wat een kabel, batterij en huis kan zijn.

#### ResultsShuffle.py:
Doet hetzelfde als ResultsDynamicSort behalve dat de inleesvolgorde van huizen willekeurig is gemaakt.

#### ResultsSort.py:
Houdt de configuratie die gemaakt is tussen welke huizen verbonden zijn met welke batterijen. vervolgens haalt het deze kabels weg. Gaat over elk netwerk heen en sorteert de huizen op basis van afstand en maakt nieuwe kabels aan.

#### TrueRandom.py:
Verbindt de huizen met een willekeurige batterij. De huizen staan in een willekeurige volgorde.