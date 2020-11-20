import numpy as np

a = np.array([(4,5,6,7),(0,1,2,3),(8,9,10,11)])
b = np.array([(4,5,6,7),(0,1,2,3),(8,9,10,11)])


print(a+b)
print(a-b)
print(a*b)
#print(a/b)

print(np.vstack((a,b)))
print(np.hstack((a,b)))

print(a.ravel())
print(sum(a.ravel()))
