#for x in range(start, end, process)
a=int(input("Enter a number to find prime or not: "))
count=0
for x in range(1,a+1,1):
    i=a%x
    if i==0:
        count+=1
if count==2 or count==1:
    print("number is prime")

else:
    print("number is not prime")
