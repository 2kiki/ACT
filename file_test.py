# # the file is test.txt try opening it with python!
import os
print(os.getcwd())

path = '/Users/Family/Desktop/PYTHON/Projects/'
filename = 'test.txt'

f = open(path+filename, "r")
#f = open('test.txt', "r")
print(f.readline())
f.close()