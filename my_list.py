import random

l =[]
for i in range(20):
    l.append(random.randint(1, 6))
print(l)

# Sort list, lowest to highest. Doesn't change list order permeantly
print('sorted list', sorted(l))
print(l)

# Slice list, [start:finish]
print(l[2:8])
print(l[3:]) # leave out finish, defaults end of list
print(l[:6]) # leave out start, defaults start of list

# Remove item from list. first item if more than one
l.remove(1)
print(l)

# pop item, removes and returns last item from list
first_item = l.pop()
print(first_item, l)