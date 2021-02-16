####################################################################

import random
print(dir(random))
agility = random.randint(1,18)
print(agility)
print("You have" , agility , "points")

if agility >= 10:
    print("You escape")
else:
    print("You trip and fall")

def dice_roll(sides):
    return random.randint(1, sides)

rca = dice_roll(20)
if rca >= 5:
    print('You win')
    print(rca)
else:
    print('You die')
    print(rca)


rca = dice_roll(15)
if rca >= 7:
    print('You win')
    print(rca)
else:
    print('You die')
    print(rca)


#print(f'You have {agility} agility points and rolled {dice_roll()}')

