def new():
    print('\n')


import pandas as pd

#it conver dictionary in to data frame

Name = ['Ved Gupta' , 'Harsh Gupta' , 'Sumedha Gupta' , 'Ajay Sharma' , 'Sudhanshu Lala']
Score = [25,35,4,6,19]
Work = ['Nalla' , 'Hotelier' , 'Designer' , 'Singer' + 'Athlites' , 'Fekna']
Id = [990 , 123 ,339 , 550 , 666]

Data = {'Name': Name , 'Score': Score , 'Work' : Work , 'Id' : Id}

d = pd.DataFrame(Data)

print(d)

#slicing rows from upper side
new()
print(d.head(3))

#slicing rows from upper side
new()
print(d.tail(2))




