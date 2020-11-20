# sum of digits using list
while(1):
    a=(input('Enter any no : '))
    b=list(a)
    c=(b[-1])
    i=a.index(c)
    s=0
    while(i>=0):
        s=s+int(b[i])
        i-=1
    print(s)
