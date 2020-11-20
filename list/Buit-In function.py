#Buit-In Functions

'''
sorted() - Returns a new sorted sequence from the items in the given seqquence
all() -    Returns True if all the elements of the supplied sequence are True
any() -    Is the converse of the all() function
bool() -   Converts the Value to a Boolean Value
chr() -    Returns the string which represents a character whose Unicode code point is an integer
open() -   Opens file for performing various file manipulations
abs() -    Returns the ansolute value of numbers
enumerate() -  Returns an enumerate object with elements and the index values provided by the user
reversed() - will reverse a sequence like list , turple , but the original sequence remains unchanged
'''

#sorted
list = [2,3,6,1,8,2,9]
turple = (2,3,6,1,8,2,9)

print("Original list : ",list)
print("Sorted list : ",sorted(list))

print("\n")

#abs
#change - Negative variable to + positive
a = -25 #negative valve
print("after abs() :", abs(a))

print("\n")

#bin
#is used to convert decimal value in to binary
dec = 20 #decimal value
print("Decimal Value to Binary : ", bin(dec))

print("\n")

#ord()
# is used to convert character to ASCII code
ch = 'x'
print("char to ASCII : ", ord(ch))

print("\n")

#reversed
#will reverse a sequence like list , turple , but the original sequence remains unchanged
list = [5,4,8,2,7]
a = reversed(list)
print(a)
print("Reversed list is : ")
for i in a:
    print(i)
print('Original list is : ',list)
#proccess same for turple

print("\n")

#all
#if all the elements of a sequence are true, then it returns true
#what is True in Pythom?
#any non-zero , non-empty value in python is true. e.g. None is true.
#only a single space is True value
list2 = [1 , 2 , 5 , 'ved' , True , '']
b = all(list2)
print('it say the all emements in list are true : ', b)

print("\n")


#any
#if any of the element in list is true it returns true
list3 = ['' , 0 , False , ' ']
c = any(list3)
print('any() fun : ',c)

print("\n")

#globals
#it gives a dictionary which contain all global variables use at the point of time
print(globals())
print("\n")
print('Global variable u used are : ')
for i in globals():
    print(i)

