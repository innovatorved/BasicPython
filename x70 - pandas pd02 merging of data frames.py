#merging of dataframe

import pandas as pd

data1 = {'BMI' :[2,3,4,5] , 'int':[50,60,55,12]  , 'CORONA':[7,8,9,4]  }
data2 = {'BMI' :[2,3,4,5] , 'int':[50,60,55,12]  , 'CORONA':[7,8,9,4]  }

d1 = pd.DataFrame(data1, index = [2001,2002,2003,2004])
d2 = pd.DataFrame(data2, index = [2005,2006,2007,2008])

merge = pd.merge(d1,d2)

print(merge)

print(pd.merge(d1,d2, on ='BMI'))
