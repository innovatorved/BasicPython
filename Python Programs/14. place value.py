#Factorial of a number

def series(x):
    result=1
    while(x>=1):
        result=result*x
        x=x-1
    return result
while(1):
    
    a=int(input('Eter a number : '))
    print('Factorial of a no. : ',series(a))
    

