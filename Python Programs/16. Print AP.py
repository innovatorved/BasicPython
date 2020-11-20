#print AP
def series(a,d,l):
    s=a
    i=0
    while(i<=l):
        print(s)
        s=s+d
        i+=1
while(1):
    a=int(input('Enter first term of AP : '))
    d=int(input('Enter difference of AP : '))
    l=int(input('Enter last term of AP : '))
    print(series(a,d,l))
        
