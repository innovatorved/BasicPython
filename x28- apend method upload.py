l=[]
while True:
    a=input("Enter a name: ")
    if a in l:
        print("",a,"is already in list")

    else:
        if a=='x':
            break
        else:
            l.append(a)

print(l)
    
