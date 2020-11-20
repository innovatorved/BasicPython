#find the value of x by equation--
print("find the value of x by equation---")
print("like equation is: ax2+bx+c=0")
a=int(input("enter the value of a in ax2 with symbole: "))
b=int(input("enter the value of a in bx with symbole: "))
c=int(input("enter the value of a in c with symbole: "))
x=b**2-4*a*c
y=x**(1/2)
z1= (-b+y)/(2*a)
z2= (-b-y)/(2*a)
print("value of +x is: ",z1)

print("value of -x is: ",z2)
#a*r**(n-1)
