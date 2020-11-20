#joining of dataframe

import pandas as pd

data1 = {'BMI' :[2,3,4,5] , 'int':[50,60,55,12]  , 'CORONA':[7,8,9,4]  }
data2 = {'MI' :[6,8,9,5] , 'ind':[55,52,89,90]  , 'CORO':[1,56,78,3]  }

d1 = pd.DataFrame(data1, index = [2001,2002,2003,2004])
d2 = pd.DataFrame(data2, index = [2001,2002,2003,2004])

joining = d1.join(d2)

print(joining)
