################################# STAGE 1 #################################
# dictionaries, 
import random
def diceroll(sides):
    return random.randint(1,sides)

def generate_attrib():
    # Returns a list of 4 integers - each integer is the best 3 out of 4 dice rolls
    l = []
    while len(l) < 4:
        l.append(highest_3())
    return l

def highest_3():
    rolls = []
    while len(rolls) < 4:
        rolls.append(diceroll(6))
    # print(rolls)
    return sum(sorted(rolls)[1:])

def print_player(player):
    print(player["name"])
    print(f"STRENGTH: {player['strength']}.")
    print(f"AGILITY: {player['agility']}")
    print(f"MAGIC: {player['magic']}")
    print(f"LUCK: {player['luck']}")
    print(f"HP: {player['hp']}")
    print(f"FATIGUED: {player['fatigued']}")
    print(f"ALIVE: {player['alive']}")

def create_charac(name):
    player = {}
    player["name"] = name
    player["strength"] = None
    player["agility"] = None
    player["magic"] = None
    player["luck"] = None
    player["hp"] = 2
    player["fatigued"] = False
    player["alive"] = True
    return player

def challenge(challenger_type, challenge_rating, player):
    #return True or False
    computer_roll = diceroll(20)
    player_roll = diceroll(20)
    player_score = player_roll + player[challenger_type]
    computer_score = computer_roll + challenge_rating

    print(f"You roll {player_roll}. Added to your {challenger_type} gives score of {player_score}. \nComputer rolls {computer_roll}. Added to challenge rating is {computer_score}.")
    if computer_score > player_score:
        return False
    else:
        return True


################################# LIST #################################
# print(generate_attrib())
# print(attrib_list)

################################# SECTION 1 #################################

player = create_charac(input("What's your name? "))

attrib_list = generate_attrib()
attrib_list.sort(reverse=True)
user_txt = ""
while 1:
    user_txt = input(f"You have rolled {attrib_list}. Do you want to reroll {min(attrib_list)}? (y/n) ")
    if user_txt == "y":
        newroll = highest_3()
        attrib_list = sorted(attrib_list)[1:] + [newroll]
        attrib_list.sort(reverse=True)
        print(f"You rolled {newroll}. Now your new attributes are {attrib_list}.")
        break
    elif user_txt == "n":
        print(f"Your final attributes are {attrib_list}.")
        break
    else:
        print("I don't understand. \nUse letters 'y' or 'n'.")

choices = ["s", "a", "m", "l"]
lookup = {"s":"strength", "a":"agility", "m":"magic", "l":"luck"}

while len(attrib_list) > 1:
    value = (attrib_list.pop())
    user_txt = ""
    while 1:
        user_txt = input(f"Which characteristic do you want {value} to be assaigned to? ")
        if user_txt in choices:
            player[(lookup[user_txt])] = value
            choices.remove(user_txt)
            break
        elif user_txt == "Briggs-Davies":
            print("ALL ATTRIBUTES MAXED.")
            break
        ######################################## MAX ATTRIBUTES ########################################
        else:
            print(f"I don't understand. \nUse valid choices: these include {choices}.")

player[lookup[choices[0]]] = attrib_list[0]
print_player(player)

################################################################################

print("Strength Challenge:10")
# print(challenge("strength", 10, player))

if challenge("strength", 10, player) == False:
    player['hp'] -= 1
    print("You have failed the challenge.")
    if player['hp'] == 0:
        print("You are dead. :(")
    else:
        print(player['hp'])
        print("You lose 1 HP.")
else:
    player['fatigued'] = True
    print(f"{player['name']} is now fatigued.")
    print("You win. \nHave some HP.")
    player['hp'] += 1

print(f"Your total HP is now {player['hp']}.")


################################################################################

print("Luck Challenge:10")
# print(challenge("strength", 10, player))

if challenge("luck", 10, player) == False:
        player['hp'] -= 1
        print("You have failed the challenge.")
        if player['hp'] == 0:
            print("You are dead. :(")
        else:
            print(player['hp'])
            print("You lose 1 HP.")
else:
        player['fatigued'] = True
        print(f"{player['name']} is now fatigued.")
        print("You win. \nHave some HP.")
        player['hp'] += 1

print(f"Your total HP is now {player['hp']}.")
