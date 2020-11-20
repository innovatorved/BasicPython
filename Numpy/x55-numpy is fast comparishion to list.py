#numpy is fast compare to list
import numpy as np
import time


size = 1000
l1 = range(size)
l2=range(size)
l3=[]

a1 = np.arange(size)
a2 = np.arange(size)

print(l1)
print(l2)
print(a1)
print(a2)

start = time.time()
result = [(x,y) for x,y in zip(l1,l2)]
print(result)
print(len(result))
for x in result:
    l3.append(sum(x))
print(l3)
print((time.time()-start)*1000)

start = time.time()
result = a1+a2
print(result)

print((time.time()-start)*1000)
