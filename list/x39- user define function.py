#user define function

def area_rectangle(a,b):
    ar=a*b
    return(ar)

def area_square(a):
    ar=a*a
    return(ar)

def area_circle(r):
    ar=3.14*r*r
    return(ar)

def area_triangle(a,b,c):
    s=(a+b+c)/2
    ar=(s(s-a)+(s-b)+(s-c))**(1/2)
    return(ar)

def area_cone(r,l):
    ar=3.14*r*l
    return(ar)

while True:
    print("Enter 1 to find area of square-")
    print("Enter 2 to find area of rectangle-")
    print("Enter 3 to find area of circle-")
    print("Enter 4 to find area of triangle-")
    print("Enter 5 to find area of cone-")

    x=int(input('Enter your Choice: '))

    if x==1:
        a=int(input('Enter the length of Square: '))
        out=area_square(a)
        print('Area = ',out,'\n' )
        
    elif x==2:
        a=int(input('Enter the length of Rectangle: '))
        b=int(input('Enter the width of Rectangle: '))
        out=area_rectangle(a,b)
        print('Area: ',out,'\n')
        
    elif x==3:
         r=int(input('Enter the radius of circle: '))
         out=area_circle(r)
         print('Area: ',out,'\n')
         
    elif x==4:
        a=int(input('Enter the length of first side: '))
        b=int(input('Enter the length of second side: '))
        c=int(input('Enter the length of third side: '))
        out=area_triangle(a,b,c)
        print('Area: ',out,'\n')

    elif x==5:
        r=int(input('Enter the radius of cone: '))
        l=r=int(input('Enter the slant height of cone: '))
        out=area_cone(r,l)
        print('Area: ',out,'\n')

        
    else:

        print('Wrong choice\n')
    

