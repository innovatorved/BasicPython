#Functions

def hey():
    print("\nFIND FIBONACCI NUMBER\n")
    a=int(input("Enter first Number:  "))
    b=int(input("Enter second Number: "))
    n=int(input("How much no. u find  "))
    for i in range(n):
        c=a+b
        a=b
        b=c
    return c

def heyy(x):
    a=1
    b=1
    for i in range(x):
        c=a+b
        a=b
        b=c
    return c

def seq(x,a,b):
    for i in range(x):
        c=a+b
        a=b
        b=c
    return c


def seqq(x,a=1,b=1): #if a or b value not define it auto detect 1
    for i in range(x):
        c=a+b
        a=b
        b=c
    return c

def fun(n,a=1,b=1):
    if n>1:
        return fun(n-1,b,a+b)
    else:
        return a+b
