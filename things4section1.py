import random
def charac_creat(name):
    character = {}
    character['name'] = name
    character['strength'] = random.randint(3,18)
    return character
print(charac_creat('Kiki'))

def diceroll(sides):
    return random.randint(1, sides)

for i in range(4):
    strength = diceroll(6)

print(strength)

############################################################################

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

############################################################################

l =[]
for i in range(4):
    l.append(random.randint(1, 6))
print(l)
print(sorted(l))
print(sorted(l[1:]))
