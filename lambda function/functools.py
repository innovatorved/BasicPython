#Lambda Functions
from functools import reduce


#reduce function (ex-1)
a = [1,2,3,4]

product = reduce((lambda x , y : x*y) , a)
print(product)
print(type(product))

#reduce (ex-2)
b = range(10,20)

ans = reduce((lambda x,y : x+y) , b)
print(ans)
print(type(ans))


