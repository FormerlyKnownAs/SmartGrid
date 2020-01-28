"""
Calculates a possible lower bound based on nearest location of other points.

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

def LowestBound(houses, batteries):

    totalCost = 0

    cableCost = 9
    
    # Finds the nearest point for each house
    for house in houses:

        shortestDistance = 100

        # Calculates distances
        for location in houses:

            if house.coordinates != location.coordinates:

                distance = abs(house.coordinates[0] - location.coordinates[0]) + abs(house.coordinates[1] - location.coordinates[1])

                if distance < shortestDistance:
                    shortestDistance = distance

        for location in batteries:

            distance = abs(house.coordinates[0] - location.coordinates[0]) + abs(house.coordinates[1] - location.coordinates[1])

            if distance < shortestDistance:
                shortestDistance = distance

            
        # Adds score for house
        totalCost += shortestDistance * cableCost

    for battery in batteries:

        shortestDistance = 100

        # Calculates distances
        for location in batteries:

            if battery.coordinates != location.coordinates:
                distance = abs(battery.coordinates[0] - location.coordinates[0]) + abs(battery.coordinates[1] - location.coordinates[1])

                if distance < shortestDistance:
                    shortestDistance = distance

        for location in houses:

            distance = abs(battery.coordinates[0] - location.coordinates[0]) + abs(battery.coordinates[1] - location.coordinates[1])

            if distance < shortestDistance:
                shortestDistance = distance

            
        # Adds score for house
        totalCost += shortestDistance * cableCost

    print(totalCost)
            