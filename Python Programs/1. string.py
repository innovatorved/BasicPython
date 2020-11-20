'''
Program  : Strings
Author   : Abhi
Date     : 21-07-2018
'''

name='"abhishek","krishna","shivam","satyam","vijay","sanjeet","ashu"'

x=(name.find('"'))
y=(name.find('"',x+1))

a=(name.find('"',y+1))
b=(name.find('"',a+1))

c=(name.find('"',b+1))
d=(name.find('"',c+1))

e=(name.find('"',d+1))
f=(name.find('"',e+1))

name1 = (name[x+1:y])
name2 = (name[a+1:b])
name3 = (name[c+1:d])
name4 = (name[e+1:f])

print (name1)
print (name2)
print (name3)
print (name4)
