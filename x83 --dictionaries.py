#dictionaries

bmi_record = {'Name':'Ved Gupta' , 'Weight': 70 , 'Height':1.75 , 'its_overweight':True}
print(type(bmi_record))

print(bmi_record)


print(bmi_record['Name'])

bmi_record['Email'] = 'vedprakashgupta463@gmail.com'
print(bmi_record)

for key in bmi_record:
    print(key,' : ',bmi_record[key])


#function for finding keys in dictionaries
val = bmi_record.keys()
print(type(val))
print(val)

bmi_record1 = {'Name':'luv u' , 'Weight': 60 , 'Height':1.45 , 'its_overweight':False , 'Email': 'luvu@faltu.com'}   

bmi_dataset = [bmi_record , bmi_record1]
print(type(bmi_dataset))
print(bmi_dataset)

print(type(bmi_dataset[0]))
