#tuples :
#1. sequence of python objects like list
#2. we use parenthesis() instead of squire brackets[]
#3. unlike list tuples are immutable meaning thier value can't be changed

x=(1,2,3,'abhi',[2,3,'nidhi'])
print(x)

#4. we can change value of list stored in tuple

x[4].append('divya')
print(x)

x[4].insert(0,'ram')
print(x)
