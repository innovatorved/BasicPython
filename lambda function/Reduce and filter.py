#Using filter and Reduce

from functools import reduce

a = range(10,100)
x = filter(lambda elem : elem%2 != 0 and elem%3==0,(a))
y = list(x)
print(y)

z = reduce((lambda x , y : x+y ),(y))
print(z)
