"""
09-01-2020


Algorithm that connects houses on separate networks to the closest available battery. 

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""

def NearestBattery(houses, batteries):

    totalCost = 0

    with open("resultaten/paths.txt","w+") as f:

        # Starts writing the results doc
        f.write("coordinates, output, route, battery, cost\n")
        
        for house in houses:

            # Makes empty list to store distance between house and battery
            distanceList = []

            for battery in batteries:

                print(battery)
                # Checks capacity and if available checks distance to battery
                if battery.capacity > house.output:
                    distance = abs(house.coordinates[0] - battery.coordinates[0]) + abs(house.coordinates[1] - battery.coordinates[1])
                    distanceList.append(distance)

                else:
                    distanceList.append(None)

            # Finds nearest available battery
            print(distanceList)
            shortestDistance = min(i for i in distanceList if i is not None)
            shortestIndex = distanceList.index(shortestDistance)

            # Sets battery and route
            house.battery = batteries[shortestIndex].coordinates
            house.route = (house.coordinates[0], house.battery[1])
            house.cost = shortestDistance * 9
            battery.capacity -= house.output

            # Writes the house data to output file
            f.write(f"{house}")
            totalCost += house.cost

    with open("resultaten/results.txt", "w+") as f:

        f.write(f"Results.\n\n")
        f.write(f"Total Distance of Cable = €{totalCost / 9}\n")
        f.write(f"Total Cost of Cable = €{totalCost}\n")

        allCost = len(batteries) * 5000 + totalCost
        f.write(f"Total cost = €{allCost}\n")


