
import random

l =[]
for i in range(4):
    l.append(random.randint(1, 6))
rolls = sorted(l[1:])

while True:
    
    ut = input(f'You have rolled {rolls}. Do you want to reroll {rolls[0]}? ')

    if ut in ['yes', 'Yes', 'y', 'Y']:
        rolls[0] = random.randint(1,6)
        print(rolls)
        break

    elif ut in ['no', 'No', 'n', 'N']:
        print(rolls)
        break
    else:
        print('I do not understand. Try again.')

print(f'Your overall value for rolls is {sum(rolls)}')