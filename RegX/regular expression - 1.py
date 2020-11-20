import re

nameage = '''
            Ved is 19 and Ajay is 20
            Anchal is 21 and Sudhanshu is 17

            '''

#specify pattern
#-----------number specified by '\d'

ages = re.findall(r'\d{1,3}' , nameage)
names = re.findall(r'[A-Z][a-z]*' , nameage)
print(ages)
print(names)

age_dict = {}
x = 0

for each_name in names:
    age_dict[each_name] = ages[x]
    x+=1

print(age_dict)
