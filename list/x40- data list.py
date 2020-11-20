l=[]

def add():
    sd=[]
    sd.append(input('Enter the name of student: '))
    sd.append(input('Enter the fathers name of student: '))
    sd.append(input('Enter the college name of student: '))
    l.append(sd)
    print('Succesfully add')

def remove():
    b=input('Enter the name of student: ')
    for x in range(0,len(l),1):
        if b in l[x]:
            c=l.pop(x)
            print(c)
            print('details removed')

while True:
    print('\nEnter 1 for add detail in list-')
    print('Enter 2 for add remove data from list-')
    print('Enter 3 for see details available on list-')
    
    a=int(input('Enter ur choice: '))

    if a==1:
        add()

    elif a==2:
        remove()
       
    elif a==3:
        print(l)

    else:
        print('Wrong choice')
