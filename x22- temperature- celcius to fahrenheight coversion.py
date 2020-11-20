#temperature conversion
b=str(input("write c for--\n cencius to fahrenheight \n write f for--\n farhenheight to celcius\n:  "))
if b=='c':
    a=input("enter temprature in cencius: ")
    b=float(a)
    f=b*(9/5)+32
    print("Temprature is: ",f,"*F")
elif b=='f':
    c=input("enter temprature in fahrenheight : ")
    d=float(c)
    e=(d-32)*(5/9)
    print("Temprature is: ",e,"*C")

else:
    print("shi choice kr bhai")

