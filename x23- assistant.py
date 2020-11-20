#assistant
a=input("Enter your Name: ")
print('hey',a)
print("what can i do for you-\npls selectthe choice: ")
print('Enter 1 for Solve A.P. problem-')
print('Enter 2 for Solve G.P. problem-')
print('Enter 3 for find area of different shapes-')
print("Enter 4 for change on temprature value-")
print("Enter 5 for find prime number between two numbers-: ")


b=int(input('your choice: '))
if b==1:
    c=float(input("Enter first term a: "))
    d=float(input("Enter difference d: "))
    e=int(input("Enter the value of n: "))
    f=c+(e-1)*d
    g=(e/2)*(2*f)
    print('value of Tn is: ',f)
    print('value of Sn is: ',g)

elif b==2:
    c=float(input("Enter first term a: "))
    d=float(input("Enter common ratio r: "))
    e=float(input("Enter the value of n: "))
    f=c*d**(e-1)
    print('value of Tn is: ',f)

elif b==3:
    print("Enter 1 for find area of circle-")
    print("Enter 2 for find area of sphere-")
    print("Enter 3 for find area of cone-")
    print("Enter 4 for find area of cylinder-")

    c=int(input("plss enter your choice: "))
    if c==1:
        d=float(input("enter the radius of the circle: "))
        e=3.14*d*d
        print('Area of circle is: ',e)

    elif c==2:
        d=float(input("enter the radius of the sphere: "))
        e=4*3.14*d*d
        print('Area of sphere is: ',e)

    elif c==3:
        print('Enter 1 if u have r,h of cone')
        print('Enter 2 if u have r,l of cone')
        d=int(input("Enter ur choice: "))
        if d==1:
            e=float(input("Enter the radius r of cone: "))
            f=float(input("Enter the height h of cone: "))
            g=((f*f)+(e*e))**(1/2)
            h=3.14*e*(e+g)
            print("Area of cone is: ",h)

        elif d==2:
            e=float(input("Enter the radius r of cone: "))
            f=float(input("Enter the length l of cone: "))
            g=3.14*e*(f+e)
            print("Area of cone is: ",g)

        else:
            print('wrong choice')

    elif c==4:
        d=float(input("Enter the radius r of cylinder: "))
        e=float(input("Enter the height h of cylinder: "))
        f=(2*3.14*d*e)+(2*3.14*d*d)
        print("Area of cylinder is: ",f)

    else:
        print('wrong choice')

elif b==4:
    d=str(input("\nwrite c for--\n cencius to fahrenheight \nwrite f for--\n farhenheight to celcius\n:  "))
    if d=='c':
        a=int(input("enter temprature in cencius: "))
        f=a*(9/5)+32
        print("Temprature is: ",f,"*F")
    elif d=='f':
        e=int(input("enter temprature in fahrenheight : "))
        c=(e-32)*(5/9)
        print("Temprature is: ",c,"*C")

    else:
        print("shi choice kr bhai")

elif b==5:
    
    c=int(input('Number start from: '))
    d=int(input('Number end to: '))
    print("Prime number is: ")
    i=0
    for x in range(c,d+1,1):
        count=0
        for y in range(1,x+1,1):
            if x%y==0:
                count+=1

        if count==2 or count==1:
            print(x)
            i+=1
    print('/nTotal prime number is: ',i)


else:
    print('wrong choice')
        
        
            
        
            
        
    
