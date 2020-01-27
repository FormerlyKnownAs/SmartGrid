"""
06-01-2020


Test document. Vergeet niet te verwijderen!

The Group Formerly Known as 'The Prince Statement'
Ben Groot, Boy Stekelbos, Momo Schaap
"""
import random as r
list1 = [[r.randint(1, 500) for i in range(10)] for i in range(10)]
print(list1)

lowestNumber = 501

for listn in list1:

    lowestSub = 501
    for number in listn:

        if number < lowestSub:
            lowestSub = number
    if lowestSub < lowestNumber:
        lowestNumber = lowestSub

print(lowestNumber)

checklist = []
for i in list1:
    print(min(i))
    checklist.append(i)
print(min(checklist))
