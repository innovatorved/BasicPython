#Exponent of list from 0 to given no
a=int(input('Enter a no : '))
p=int(input('Enter a power : '))

b=list(range(a))
y=[]
i=0
for i in b:
    y.append(i**p)
print(y)
