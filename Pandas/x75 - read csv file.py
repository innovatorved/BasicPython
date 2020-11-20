#Data Mugling

import pandas as pd

read = pd.read_csv('D:\\file.csv' , index_col=0)
print(read)

#change csv to html
read.to_html('edu.html')


