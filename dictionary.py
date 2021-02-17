import random

# Create empty dictionary
my_dictionary = {}

# add some items
my_dictionary['name'] ='kiki'
my_dictionary['height'] ='perfect'

print(my_dictionary)

# Create dictionary from function
def charac_creat(name):
    my_dict = {}
    my_dict['name'] = name 
    my_dict['strength'] = random.randint(0,6)
    my_dict['agility'] = random.randint(0,6)
    my_dict['magic'] = random.randint(0,6)
    my_dict['luck'] = random.randint(0,6)
    my_dict['hp'] = random.randint(0,6)

    return my_dict

player = charac_creat('kiki')
print(player)
# Iterate through dictionary, remember a dictionary is made from key, value pairs
for item in player.items():
    print(f"item is a pair of values {item}")

# or can split pair into 2 variables
for key, value in player.items():
    print(f"key is {key}. value is {value}")

# Can iterate over just keys or values
for key in player.keys():
    print(f"key is {key}")

for value in player.values():
    print(f"value is {value}")