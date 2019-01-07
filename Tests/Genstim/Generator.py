import numpy as np
import random


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
