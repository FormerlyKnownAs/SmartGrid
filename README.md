# SmartGrid
The SmartGrid assignment repository for the group 'The Group Formerly Known as 'The Prince Statement' '

Ben Groot, Boy Stekelbos, Momo Schaap

De case die ons team gegeven is heet SmartGrid, het objectief voor dit probleem is zo efficient mogelijk huizen, die energie produceren te verbinden aan batterijen die deze energie opslaan. De batterijen hebben gelimiteerde capaciteit dus is het van belang dat de correcte configuratie van huizen verbonden aan een batterij gekozen wordt. Zonder dit te doen is er risico van het overlaten van een of twee huizen die bij geen enkele batterij er meer in past. 


Resultaten reproduceren:

    python main.py is het basis formaat.
    
    pthon  main.py 10 geeft aan hoeveel iteraties het programma moet doen voordat het klaar is.
    
    python main.py 10 wijk1  hier heb je de keuze van wijk1 tot wijk3
    
    python main.py 10 wijk1 1 besluit de keuze van algoritme, waarbij 1 ot 6 opties zijn.

    python main.py 10 wijk1 1 3 besluit welke optimizer gebruikt wordt, met keuzes van 1 tot 3

    python main.py 10 wijk1 1 3 2 kiest de hillclimber methode die gebruikt wordt, met keuzes van 1 en 2

    Keuzes van algoritmes:
    1: TrueRandom
    2: BatterySearch
    3: bestFitNetwork
    4: HouseSearchHybrid
    5: HouseSearchFull
    6: NetworkSearch

    Keuzes van optimizers:
    1: ResultsShuffle
    2: ResultsSort
    3: ResultsDynamicSort

    Keuzes van hillclimbers:
    1: CornerChange
    2: CornerPositionChange



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
> data - hier staat onze csv data van de opdracht
> resulaten - hier staat onze output.





