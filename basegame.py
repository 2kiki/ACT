################################# STAGE 1 #################################
import time

name = input('What is your name? -> ')
print(f'Welcome {name}, Hero of Greece. \nDestined to slay the Minutaur and save us all.')
time.sleep(3) 

################################## STAGE 2 #################################

print('You have now entered the lair of the Minutaur...')
time.sleep(3) 
print('In the murky darkness, you discover two corridors.')
time.sleep(3)
print('The door to the left is long and winded, you cannot decipher how far it stretches. \nThe door to the right is short; you can make out a small doorway at the rear.')
time.sleep(5)

while True:
    lor = input('It is impossible to choose. Yet you must. Which way will you go? -> ')
    if lor == 'l':
        print('You begin to make your way to through the corridor to the left. \nAs you turn the corner, you are disappointed to discover another lengthy hall. \nNevertheless, you drag your feet forward, finally reaching the end. Hoorah!')
        time.sleep(5)
        print('However, your celebration dies as you notice another replica corridor.')
        time.sleep(3)
        print('You have no choice but to keep moving forward.')
        time.sleep(5)
        print('You reach the final corner. \nAs you gaze into the distance, you unearth a small gap in the wall.')
        time.sleep(3)
        print('A door!')
        time.sleep(2)
        print('Then you realise, with a shock, the corridor you have entered was the one to the right of your starting point!')
        time.sleep(5)
        print('You have walked five miles for a door that was metres away, yet at least you did not encounter any beasts.')
        ########## - HP, LOW HP COLLAPSE ##########
        break
    elif lor == 'r':
        print('You begin to make your way to through the corridor to the right. \nAs you approach the door, you notice the winding corridor that snakes around the maze.')
        time.sleep(5)
        print('Perhaps the corridor to the left was an elaborate and surely exhaustive route to the same destination. \nBe thankful your chose correctly this time...')
        break
    else:
        print('I do not understand.')

print('You swallow your fear and enter into the opening...')
time.sleep(3)
print('You amble down the tunnel. \nThe walls are damp and illogically high. \nYour eyes adjust and you are almost certain there is a figure in the darkness. \nThe figure does not look human, or hero, yet it certainly cannot be the Mintuar...')
time.sleep(8)
print('To your left the floor has corroded to reveal an underground pathway. \nTo your right is a wider hall, where it leads to is unknown.')
time.sleep(5)
print('You could sneak past the figure to the right, leap to the left or use your Greek brawn to fight.')
while True:
    harpy = input('Sneak, fight or jump? -> ')
    if harpy == 's':
        print('You lower to your hands and knees before pressing your stomach onto the ground. \nIn a military')
        time.sleep(5)
        ########## A, LOW A LOSE ##########
        break
    elif harpy == 'f':
        print('You fight')
        time.sleep(5)
        ########## S, LOW S LOSE ##########
        break
    elif harpy == 'j':
        print('You jump')
        ########## - HP, LOW HP COLLAPSE ##########
        time.sleep(5)
        break
    else:
        print('I do not understand.')
