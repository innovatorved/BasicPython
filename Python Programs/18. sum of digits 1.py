# sum of digits using list
while(1):
    a=(input('Enter any no : '))
    b=len(a)        #to store length of string
    s=0
    while(b>0):
        s=s+int(a[b-1])
        b-=1
    print(s)
