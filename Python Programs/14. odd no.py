#odd no
def number(x):
    a=(int(x)%2)
    
    if(a==0):
        print(x,' is even no')
    elif(a==1):
        print(x,'is odd no')
    else:
        print('Wrong choice')
    
while(1):
    a=(input('Enter a no : '))
    number(a)
