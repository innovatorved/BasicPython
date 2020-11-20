#random module genrates pseudo-random numbers for various distributions
import random



#random.randrange(x) - Genrates a random integer within the given range
num = random.randrange(99)
print(num)

#random.rangrange(start , stop , step) - Returns a randomly selected element
ram = random.randrange(1 , 99 , 20)
print(ram)

#random.randint(x , y) - Returns the random integer such that x <= N <=y
initt = random.randint(0,22)
print(initt)
 

#random.getstate - returns an object which captures the current internal state of the genrator
print(random.getstate)

#random.uniform(x , y) - returns a random floating point no. A such that x<=A<=y for x<=y and y<=A<=x for y<x
print(random.uniform(4,9))
