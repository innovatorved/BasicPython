#sum of min and max no
x=[]
a=int(input('how much numbers you have : '))
t=0
for i in range(a):
    x.append(int(input('Enter no : ')))
    t=x[i]+t
print(x)
m=0
M=[]
n=0
N=[]
for i in range(a):
    if(x[i]>=7):
        m=m+x[i]
        M.append(x[i])
    else:
        n=n+x[i]
        N.append(x[i])
print(m)
print(M)
print(n)
print(N)
print(x)
print(t)
