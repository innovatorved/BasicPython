#concrete add 2 data frames with index

import pandas as pd

data1 = {'BMI' :[2,3,4,5] , 'int':[50,60,55,12]  , 'CORONA':[7,8,9,4]  }
data2 = {'BMI' :[6,8,9,5] , 'int':[55,52,89,90]  , 'CORONA':[1,56,78,3]  }

df = pd.DataFrame(data1,index = [2001,2002,2003,2004])
dd = pd.DataFrame(data2,index = [2005,2006,2007,2008])

Con = pd.concat([df,dd])
print(Con)



