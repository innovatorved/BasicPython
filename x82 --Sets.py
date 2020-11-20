#sets
#set is a collection of unique items nothing is duplicated
#we are not check index in sets

batsman = {'Rohit' , 'Virat' , 'Hardek' , 'Rahul' , 'Dhoni'}

print('Type: ',type(batsman))

#check element is in set
print('Dhoni' in batsman)

bowlers = {'Bumrah' , 'Ishant' , 'Ravindra' , 'Hardek'}
print('Type: ',type(batsman))

#Intersection of two sets
#it returns common value in both sets
all_rounders = batsman.intersection(bowlers)

print('Type: ',type(all_rounders))
print(all_rounders)

players = batsman.union(bowlers)  #add both sets

print('Type: ', type(players))
print(players)

#if we write one element two times in sets only one item show if we print set
bowlers = {'Bumrah' , 'Ishant' , 'Ravindra' , 'Hardek' ,'Bumrah'}
print(bowlers)
