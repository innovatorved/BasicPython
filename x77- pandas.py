from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')

file = read_csv('D:\\file.csv' , index_col=0)

print(file)

df = file.head(5)

df =df.set_index(['FATHER NAME'])

print(df)

sd =df.reindex(columns=['ADHAR NO.','MOBILE NO.'])

print(sd)

db = sd.diff(axis=1)
db.plot(kind = 'bar')
plt.show()
