#string : collection of characters.
#a='Abhishek'
#list : collection of anything.
#b=[1,2,3,[1,12,13],'abhi',['nidhi','divya',1234]]
items=[]
while True:
    a=input('if want to enter item in list then yes or no : ')
    if (a=='yes'):
        l=input('Enter item name : ')
        if(l in items):
            print('item is already in list')
        else:
            items.append(l)
    else:
        print(items)
        break
    
