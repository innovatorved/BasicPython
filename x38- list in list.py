#to access list in list
#list under list
l=[]

while True:
    print("\nenter 1 for adding student information-")
    print("enter 2 for remove student information-")
    print("enter 3 for showing the list-")
    ch=int(input('Enter your choice- '))
    if ch==1:
        sd=[]
        sd.append(input('\nEnter the name of student: '))
        sd.append(input('Enter the college name of student: '))
        sd.append(input('Enter the branch of student: '))
        l.append(sd)

    elif ch==2:
        a=input('Enter the name of student: ')
        for x in range (0,len(l),1):
            b=l[x]
            if a in b:
                l.remove(b)
                print('data were deleted')


            else:
                print('information not available')
        


    elif ch==3:
        print('list is: ',l)


    else:
        print('wrong choice')
