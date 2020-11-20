#program for find factorial of a number
a=int(input("Enter a number to find its factorial: "))
b=1
for a in range(a,0,-1):
    b=b*a
    
print(b)
