list = [0,1,2,3,4,5,6]

print(list)

#accessing list by last uses - symbol

print(list[-2])

#accesing list from the middle by :

print(list[2:5])
#creating a duplicate list B

B = list
print('Duplicate list',B)

#if we stop change then use
C = [item for item in list]
print('by coping',C)

#if we change in first list then it also change in duplicate list

list[0] = list[5]
print('Change in first change',list)

print('the vale of secound list is also change:',B)

#if we stop change the use
print('But not change in this list',C)
