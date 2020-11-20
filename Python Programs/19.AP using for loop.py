#for loop : start stop step argument
def ap(a,l,d):
    s=0
    for s in range(a,l+1,d):
        print(s)
while(1):
    a=int(input('Enter a no : '))
    l=int(input('Enter a no : '))
    d=int(input('Enter a no : '))
    ap(a,l,d)
