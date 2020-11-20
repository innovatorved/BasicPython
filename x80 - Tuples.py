#turple
#turple is immutable
#once u defined turple u cannot change its elements 

bmi_cat = ('Underweight' , 'Normal', 'Overweight' ,'very Overweight')

#type
print('Type: ',type(bmi_cat))

#access element of turple

print(bmi_cat[1])  #we use positive value

print(bmi_cat[-2]) #and we also use negative value

print(bmi_cat[0:3])#indexing range

print(bmi_cat.index('Normal')) #searching index of value

#for searching any element was in turple or not
#it is Case sensitive
print('Very underweight' in bmi_cat)  #it return Boolean value

