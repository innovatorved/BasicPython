#find area of triangle
a=int(input("Enter first Side: "))
b=int(input("Enter second Side: "))
c=int(input("Enter third Side: "))
s=(a+b+c)/2
a1=(s-a)
a2=(s-b)
a3=(s-c)
A= s*a1*a2*a3
print("area of triangle is: ",A**(1/2))
