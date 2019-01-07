import random
from array import *
my_array = array('i', [	1,2,3,4,5])

y = random.randrange(0, 101, 2)
for x in range(0, 3):
    print(y)

list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
for list in list_of_lists:
    for x in list:
        print (x)