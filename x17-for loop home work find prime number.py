print("find prime number bet-")
a=int(input('start from: '))
y=int(input('End to: '))
b=0
print("list of prime numbers is: ")
for a in range(a,y+1,1):
    count=0
    for x in range(1,a+1,1):
        i=a%x
        if i==0:
            count+=1
    if count==2 or count==1:
        print(a)
        b+=1
    

print("\ntotal prime number is: ",b)

