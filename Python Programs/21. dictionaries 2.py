# dictionaries : keys and value method
d={'name':'abhishek','age':'23 years','height':'182cm'}

# 1. make a list of all keys:
# A
print(d.keys())
#B
for i in d.keys():
    print(i)

# 2. make a list of all values:
#A
print(d.values())
#B
for i in d.values():
    print(i)

# 3. get keys and values:
# item method : give list of tuples of keys and values

print(d.items())

#or
for i,j in d.items():
    print('key is ',i,'and','value is ',j)

for i,j in sorted(d.items()):
    print('key is ',i,'and','value is ',j)
