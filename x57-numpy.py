import numpy as np

a = np.array([(4,5,6,7),(0,1,2,3),(8,9,10,11)])

print(a)

print("Dimension of Array: ",a.ndim)

print("byte size: ",a.itemsize)

print("datatype: ",a.dtype)

print("Size of the array: ",a.size)

print("Shape of the array: ",a.shape)

print(type(a))

#Reshape

b = a.reshape(6,2)
print(b)

#slicing(to find one element from array)

c = a[1,2]
print(c)

d = a[0:2,3]
print(d)

#use of linespacing

e = np.linspace(1,9,18)
print(e)

#maximum value

print(a.max())

#minimum value

print(a.min())

#sum value

print(a.sum())

#sum of one axis

print(a.sum(axis=1))

#square root

print(np.sqrt(a))
print(np.sqrt(a[0,0]))

#standard davision how much all value closest to mean

print(np.std(a))

