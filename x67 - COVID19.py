# Author: Next In

import requests
from bs4 import BeautifulSoup
import pandas as pd
from prettytable import PrettyTable

from matplotlib import pyplot as plt
print('Author : Ved Prakash Gupta\n')
print('Please Connect Device with Internet\n')
print('Connecting To Ministry Of Health....\n\n')
url = 'https://www.mohfw.gov.in/'
web_content = requests.get(url).content
#print(web_content)
print('Data succesfully fetch by Ministry of Health India\n\n\n')
soup = BeautifulSoup(web_content , "html.parser")
#print(soup)

extract_contents = lambda row: [x.text.replace('\n','')for x in row]

stats = []  #list

all_rows = soup.find_all('tr')  #find all table in rows
#print(all_rows)

for row in all_rows:
    stat = extract_contents(row.find_all('td'))
    #print(stat)
    if len(stat) == 5:
        stats.append(stat)
   
del(stats[len(stats)-1])
#print(stats)


new_column = ['Sr.no.' , 'States/UT' , 'Confirmed' , 'Recovered' , 'Death']
state_data = pd.DataFrame(data = stats , columns = new_column)
print(state_data)



state_data['Confirmed'] = state_data['Confirmed'].map(int)
state_data['Recovered'] = state_data['Recovered'].map(int)
state_data['Death'] = state_data['Death'].map(int)

table = PrettyTable()
table.field_names = (new_column)

for i in stats:
    table.add_row(i)

table.add_row(["","Total", 
               sum(state_data['Confirmed']), 
               sum(state_data['Recovered']), 
               sum(state_data['Death'])])
print(table)

confirm = []
recover = []
death = []

for x in stats:
    confirm.append(int(x[2]))
    recover.append(int(x[3]))
    death.append(int(x[4]))


plt.figure(figsize = (15,10))
plt.barh(state_data['States/UT'],state_data['Confirmed'].map(int),align = 'center',color='lightblue',edgecolor='blue')

plt.title('Total Confirmed Case StateWise',fontsize = 18)
plt.xlabel('No. of Confirmed cases',fontsize = 18)
plt.ylabel('States/UT',fontsize = 18)
plt.xticks(fontsize = 8)
plt.yticks(fontsize = 7)

for index, value in enumerate(state_data['Confirmed']):
    plt.text(value, index, str(value), fontsize = 8)

c=(sum(confirm))
r=(sum(recover))
d=(sum(death))
re=(c-r)

group_size = [c,r,d,re]

group_labels = ['Confirmed\n' + str(c), 
                'Recovered\n' + str(r), 
                'Death\n'  + str(d),'Total Active Cases\n' +str(re)]
                
custom_colors = ['skyblue','yellowgreen','tomato','orange']

plt.figure(figsize = (5,5))
plt.pie(group_size, labels = group_labels, colors = custom_colors, startangle=60 ,explode=(0,0.1,0.1,0.5))
central_circle = plt.Circle((0,0),0.5, color = 'white')
fig = plt.gcf()
fig.gca().add_artist(central_circle)
plt.rc('font', size = 12) 
plt.title('Nationwide total Confirmed, Recovered and Deceased Cases', fontsize = 16)
plt.show()

