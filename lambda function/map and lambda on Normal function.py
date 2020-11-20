#Map in lamda can be used in normal functions as well

def add(a):
    return a**2 + a+3

b = range(10,20)
x = filter((lambda elem : elem > 0 and elem%2 != 0) , (b))
y = list(x)
print(y)

z = map(add , y)
print(z)
print(list(z))
