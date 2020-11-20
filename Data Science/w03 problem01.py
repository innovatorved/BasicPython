#find BMI and represent the table

w=float(input("Enter your weight in kg: "))
h=input("Enter F for height entering in Foot \nEnter M for height entering in Metre: ")

if h=="F":
    f=float(input("Enter the height in foot\n like 5.9foot: "))
    m=f*0.3048
    print("your height in metere is: ",m)

elif h=="M":
    m=float(input("\nEnter the height in metre: "))
    f=m*3.28084
    print("your height in foot is: ",f)

else:
    print("Wrong Choice!")

BMI=w/(m**2)
print("BMI is: ",BMI)

if BMI < 18.5:
    print("\nUNDERWEIGHT")

elif 18.5 <= BMI < 25:
    print("\nNORMAL")

elif 25 <= BMI <30:
    print("\nOVERWEIGHT")

elif BMI >= 30:
    print("\nVERY-OVERHEIGHT")

else :
    print("Wrong fied!")
