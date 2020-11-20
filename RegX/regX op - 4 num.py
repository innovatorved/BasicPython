import re

marks = "1 2345"

#\d set to only one num characte
print("Matches: ",len(re.findall("\D", marks)))


marks1 = "123 1234 12345 123456 1234567"

#se the size of nummber
print("Matches1: ",len(re.findall("\d{5,7}", marks1)))


#check number is valid for india or not
number = "+917007868719"

#if we define the length of any number we use -- \d
if re.search("[+91]\d{10}", number):
    print("Number is valid for india !")


#\w [a-zA-Z0-9_]
#\W [^a-zA-Z0-9_]
phone="412-555-1212"

if re.search("\d{3}-\d{3}-\d{4}",phone):
    print("phone number is valid")


#retuen all the number between then in list
phones = "1234568796"
out =  re.findall("[0-5]",phones)
print(out)

