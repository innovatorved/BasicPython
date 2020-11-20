#odd no
while(1):
    a=int(input('Enter a no : '))
    i=a
    t=0
    while(i>0):
        ans=a%i
        if(ans==0):
            t=t+1
        i=i-1
    if(t==2):
        print(a,'is prime no')
    elif(t>2):
        print(a,'is divisible by',(t-2),'numbers')
