# SmartGrid
The SmartGrid assignment repository for the group 'The Group Formerly Known as 'The Prince Statement' '

Ben Groot, Boy Stekelbos, Momo Schaap

De case die ons team gegeven is heet SmartGrid, het objectief voor dit probleem is zo efficient mogelijk huizen, die energie produceren te verbinden aan batterijen die deze energie opslaan. De batterijen hebben gelimiteerde capaciteit dus is het van belang dat de correcte configuratie van huizen verbonden aan een batterij gekozen wordt. Zonder dit te doen is er risico van het overlaten van een of twee huizen die bij geen enkele batterij er meer in past. 


bestFitNetwork.py:

Algorithm that connects houses on separate networks to the battery that fits it best.

hillclimbSortv2.py:

Neemt een redelijk geoptimaliseerde oplossing en vervolgens verandert het de hoek die de kabels nemen om de connectiepunt van het netwerk te bereiken.(Mogelijk ook de inleesvolgorde veranderen van huizen)

lineTrackRandom.py:
Maakt en slaat een lijn op van begin punt tot eind punt waar de hoek die de lijn neemt  willekeurig is terwijl deze altijd vast staat bij de normale lineTrack.

lowerBoundCalculator.py:
Berekent de lower bound van een wijk gebaseerd op de afstand tussen huizen en batterijen, neemt de capaciteit van de batterijen niet in cosideratie, waardoor dit alleen de theoretische lowerbound is.

nearestBatterySimple.py
Een simpel algoritme dat huizen verbindt met een batterij gebaseerd op de afstand tussen het huis en de dichtstbijzijnde batterij locatie en de capaciteit.

nearestHouseReworkv2.py:

----Moet nog gemaakt worden

nearestNetworkCluster.py:
Een algoritme dat huizen verbindt op basis van afstand met andere huizen, dit vormt dat uiteindelijk een cluster van huizen wat leidt tot het efficient leggen van kabel.

nearestNetworkShuffle.py:

Houdt de configuratie die gemaakt is tussen welke huizen verbonden zijn met welke batterijen. Vervolgens verwijdert het de kabels en maakt nieuwe kabels aan gebaseerd op de afstand tussen het huis en de dichstbijzijnde netwerk punt wat een kabel, batterij en huis kan zijn.

nearestNetworkv3Random.py:
Genereert de initiele configuratie waar andere algoritmen uiteindelijk mee verder werken. De volgorde van het inlezen van de huizen is willekeurig, vervolgens maakt het verbindingen tussen huizen en batterijen op basis van afstand. dit generereert een netwerk van kabels die vervolgens ook meegenomen worden in de afstandsberekening.

mst.py(conceptueel onverenigbaar):
Niet volledig afgemaakt, maar aangepast om de configuratie tussen huizen en batterijen te onthouden en te accepteren in het programma. Deze als nodes in het programma te stoppen om vervolgens de minimum spanning tree te vinden.

nearestNetworkSortOrderList.py :
Neemt een json bestand, waarin de netwerken van huizen en batterijen al aangemaakt zijn. Vervolgens worden de kabels in deze netwerken weggehaald. Dan wordt er over elk netwerk en elk huis geloopt waarbij elk huis nieuwe connecties maakt naar het netwerk toe, vervolgens zoeken de volgende huizen connectiepunten aan het netwerk, waar elke kabel die deel uitmaakt van het netwerk een connectiepunt is.



SmartGrid bevat de volgende mapjes en files:

- __init__.py - staat ons toe files te importeren
- .gitignore - Vermijd het pushen van bepaalde files
- main.py - De file die gerunt wordt
- README.md - deze file
- requirements.txt - de file die pip instalaties doet
- TODO.md - met stappen die nog genomen moeten worden
> __pycache__ - negeer deze folder, hier staan compilaties in
> code - hier staan onze .py bestanden om, buiten main.py om.
    > __pycache__ - negeren
    > algorithms - onze algoritmes, die daadwerklijk dingen toepassen
    > classes - onze objecten, zoals huizen, netwerken en batterijen
    > visualization - al onze code die visualizeert
    > zDELETEBEFOREHANDINGIN - test files die verwijderd moeten worden
> data - hier staat onze csv data van de opdracht
> resulaten - hier staat onze output.




Resultaten reproduceren:
-python main.py ----------  is altijd het begin.
-pthon main.py 10 --------  geeft aan hoeveel iteraties het programma moet doen voordat het klaar is.
-python main.py 10 wijk1--  hier heb je de keuze van wijk1 tot wijk3
-python main.py 10 wijk 1-  besluit de keuze van algoritme, waarbij 1 tot 4 opties zijn.

