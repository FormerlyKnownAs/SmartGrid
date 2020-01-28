# SmartGrid
The SmartGrid assignment repository for the group 'The Group Formerly Known as 'The Prince Statement' '

Ben Groot, Boy Stekelbos, Momo Schaap

De case die ons team gegeven is heet SmartGrid, het objectief voor dit probleem is zo efficient mogelijk huizen, die energie produceren te verbinden aan batterijen die deze energie opslaan. De batterijen hebben gelimiteerde capaciteit dus is het van belang dat de correcte configuratie van huizen verbonden aan een batterij gekozen wordt. Zonder dit te doen is er risico van het overlaten van een of twee huizen die bij geen enkele batterij er meer in past. 


## Gebruiksaanwijzing:

    Cmd command format: python main.py ITERATIONS WIJK RANDOMIZER OPTIMIZER FINALIZER
    - Iterations: geeft aan hoeveel iteraties het programma moet doen voordat het klaar is. Dit is een nummer
    - Wijk: geeft de wijk mee als input. Dit is de prefix van een wijk (bijv. wijk1)
    - Randomizer: besluit het basis algoritme, waarbij 1 tot 6 de opties zijn.
    - Optimizer: Besluit welke heuristiek gebruikt wordt om het randomizer resultaat te verbeteren, met keuzes van 1 tot 3
    - Finalizer: Besluit welke heuristiek gebruikt wordt om kleine aanpassing te maken aan een optimized resultaat, met keuzes van 1 en 2

    Een input zonder argumenten runt de volgende set up: python main.py 100 wijk1 6 3 2

    Keuzes van randomizers:
    1: TrueRandom           -   Compleet willekeurige oplossing
    2: BatterySearch        -   Verbindt huizen in een willekeurige volgorde aan dichtsbijzijnde batterij
    3: bestFitNetwork       -   Verbindt huizen in een willekeurige volgorde met de batterij met het meeste capaciteit
    4: HouseSearchHybrid    -   Verbindt vanuit de netwerken met het dichtsbijzijnde huis. De laatste tien huizen zijn willekeurig.
    5: HouseSearchFull      -   Verbindt vanuit de netwerken met het dichtsbijzijnde huis.
    6: NetworkSearch        -   Verbindt huizen in een willekeurige volgorde met het dichtsbijzijnde netwerk punt.

    Keuzes van optimizers:
    1: ResultsShuffle       -   Houdt de configuratie van netwerken, maar legt kabels opnieuw aan in willekeurige volgorde.
    2: ResultsSort          -   Houdt de configuratie van netwerken, maar legt kabels opnieuw aan op afstand tot batterij.
    3: ResultsDynamicSort   -   Houdt de configuratie van netwerken, maar legt kabels opnieuw aan op afstand tot netwerk punten.

    Keuzes van finalizers:
    1: CornerChange         -   Neemt een optimizer oplossing en verandert een willekeurige hoek.
    2: CornerPositionChange -   Neemt een optimizer oplossing, verandert willekeurige hoek of verplaats huis in aanlegvolgorde.



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





