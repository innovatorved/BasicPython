print("hlo world")
print("My self VED")
while True:
        print("\nenter 1 to find sum of two numbers-")
        print("enter 2 to find subtract of two numbers-")
        print("enter 3 to find multiple of two numbers-")
        print("enter 4 to find divide of two numbers-")
        a=int(input('Enter a number:\t'))
        if a==1:
            b=int(input('Enter 1st number:\t'))
            c=int(input('Enter 2nd number:\t'))
            print('\nsum is:\t',b+c)

        elif a==2:
            b=int(input('Enter 1st number:\t'))
            c=int(input('Enter 2nd number:\t'))
            print('\nsubtraction is:\t',b-c)

        elif a==3:
            b=int(input('Enter 1st number:\t'))
            c=int(input('Enter 2nd number:\t'))
            print('\nmultiply is:\t',b*c)

        elif a==4:
            b=int(input('Enter 1st number:\t'))
            c=int(input('Enter 2nd number:\t'))
            print('\ndivide is:\t',b/c)

        else :
            print("\nwrong choice\n")

