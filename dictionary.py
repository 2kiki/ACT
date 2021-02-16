import random

player1 = input('Name of player 1 = ')

def charac_creat(name):
    player1attrib = {"strength":0, "agility":0, "magic":0, "luck":0, "hp":0}    
    player1attrib['strength'] = random.randint(0,6)
    player1attrib['agility'] = random.randint(0,6)
    player1attrib['magic'] = random.randint(0,6)
    player1attrib['luck'] = random.randint(0,6)
    player1attrib['hp'] = random.randint(0,6)

    return player1attrib

# for sub in player1attrib:
#     for key in sub:
#         sub[player1attrib] = int(sub[player1attrib])

print(charac_creat(player1))

# def diceroll(sides):
#     return random.randint(1, sides)

# for i in range(4):
#     strength = diceroll(6)

# print(strength)

# stren =[]
# for i in range(4):
#    stren.append(random.randint(1, 6))
# print(stren)
# print(sorted(stren))
# #print(l[0:1])