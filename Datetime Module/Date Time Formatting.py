#Date Time Formatting
import datetime

current_date = datetime.datetime.now()
print(type(current_date))
print(current_date)


formatted_date = current_date.strftime("%A/%B/%Y")
#the date will be printed in this format
#________ .strftime("%A/%B/%Y") used for changing date to string
#strftime() is used to convert datetime object into string type

print(formatted_date)
print(type(formatted_date))
