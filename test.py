#name = "Super Sofia"
agility = 10
print(type(agility))
fatigued = False
print(type(fatigued))
l = ["sof", "is", "the", "best"]
print(len(l))

person ={'name':None, 'age':None, 'height':None}
person['name'] = 'sofia'
person['age']=16
person['height'] = 'very small'

for attrib in person.items():
    print(attrib)

person2 ={'name':None, 'age':None, 'height':None}
person2['name'] = 'smelly froggie'
person2['age']=62
person2['height'] = 'under six foot'

for attrib in person2.items():
    print(attrib)

####################################################################

import random

strength = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
milk = [True, False]
sugar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
coffee ={'strength':None, 'milk':None, 'sugar':None}
coffee['strength'] = random.choice(strength)
coffee['milk']=random.choice(milk)
coffee['sugar'] = random.choice(sugar)

for attrib in coffee.items():
    print(attrib)

