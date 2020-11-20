def factorial(n):           # find factorial of a number
    y=1
    for x in range(n ,0,-1):
        y=y*x
    return(y)

def factorial_recursive(n):
    if n>1:
        return n*factorial_recursive(n-1)
    else:
        return 1

def compute_ratio(x,n):
    a=factorial_recursive(n)
    b=x**n
    c=b/a
    return c

def compute_sum(x,N):
    sum=0
    for i in range(N):
        sum +=compute_ratio(x,i+1)

    return (sum+1)
        
def compute_sum_epsilon(x,epsilon):
    sum=1
    i=1
    while True:
        data = compute_ratio(x,i)
        sum += data
        i+=1
        if data < epsilon:
            break
    return sum

p=1.2
q=2.3

v1 = compute_sum(p,100) * compute_sum(q,100)
v2 = compute_sum(p+q,100)

print("v1 is : ",v1)
print("v2 is : ",v2)
print("v1-v2 is : ",v1-v2)
