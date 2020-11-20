#prime no

while(1):
    number=int(input('Enter a no : '))
    power=int(input('Enter power : '))
    i=power
    ans=number
    while(power>1):
        ans=ans*number
        power=power-1
    print(number,'to the power ',i,'is',ans) 
