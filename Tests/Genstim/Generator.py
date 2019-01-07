import numpy as np
import random
# make and print out two-dimensional array from 0 to 9 using function np.random.random_integers, 3 arguments (min, max, size)
# mylist = np.random.random_integers(0, 9, (2, 10)) # initialize variable c with function np.random.random_integers and print out result
# print (mylist) # print and check the result
# compare all numbers on first line using for loop


# initialize one-dimensional array from 0 to 9 using function np.random.random_integers, 3 arguments (min, max, size)
#mylist = np.random.random_integers(0, 9, 10)
#print out result and check the result
#print (mylist)

m=10
mass=[]
corrans=[]
k=0

for i in range(m):
   mass.append(random.randint(0,10)) 
   print(mass[i])
for i in range(m):
   corrans.append(random.randint(0,10)) 
   print(corrans[i])

for i in range(8):
    k=k+1
    if (mass[i]==mass[k+1]):
        corrans[i]=1
    else:
        corrans[i]=0
    print(mass[i],mass[k+1],corrans[i])