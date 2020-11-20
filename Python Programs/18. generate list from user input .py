# generate list from user input
while(1):
    a=[]
    i=0
    t=0
    while(t==0):
        c=input('Enter a name : ')
        a.insert(i,c)
        i+=1
        t=int(input('Enter 1 to show and 0 to add list : '))
    print('Entered name is : ',a)
        
