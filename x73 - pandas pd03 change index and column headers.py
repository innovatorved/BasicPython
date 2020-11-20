#change index and header

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

data = {'day' : [1,2,3,4] , 'Visitors' : [222,320,190,350] , 'Bounce_rate' : [20,45,60,10]}

df = pd.DataFrame(data)

print(df)

#set index
a=df.set_index('Visitors' , inplace=True)  
print(df)

#edit column name

dd = df.rename(columns={'day':'Date'})
print(dd)

#visulisation
df.plot()  
plt.show()




