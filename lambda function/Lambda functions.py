#Lambda Functions
#map function

#map function
a = [1 , 2 , 3 , 4]   #list

x = map(lambda elem : elem**2 , a)
print(x)
print(list(x))


#filter function (ex-1)
b = [1,2,3,4,5,6,7,8,9]

y = filter(lambda elem : elem<5 , b )
print(y)
print(list(y))


#filter (ex-2)
c = range(-1000 , 999)

z = filter(lambda elem:elem%2==0 and elem/3!=0 , c)
print(z)
print(list(z))
