'''
Datetime : the datetime module is used to work with dates,
times in the recent past to the near future.
'''

import datetime

#print today date with current time present date and time
tim = datetime.datetime.today() 
print(tim)

#change number into a date and time formate datetime.datetime(year , month , date , hour , min , sec)
new = datetime.datetime(2002 , 1 , 4 , 7 , 5)
print(new)

#subtract 2 different datetime
sub = tim - new
print(sub)


#Present Date and Time
present_date = datetime.datetime.now()
print(type(present_date))
print("present_date : ",present_date)

#read future dates (datetime.timedelta() fun may use)
future_date = present_date + datetime.timedelta(days = 455 , hours = 13 , minutes = 45 , seconds = 36)
print(future_date)

print(future_date - present_date)
