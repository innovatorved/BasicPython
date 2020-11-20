import pandas  as pd
def con(data):
    if data==None:
        return'Not Avail'
    return data

data = pd.read_excel('D:\\GGP.xlsx','Sheet1',coverters ={'ENROLLMENT NO.':con})

data=data.set_index(['NAME'])

df =data.head(20)

sd = df.reindex(columns=['ENROLLMENT NO.','DATE OF BIRTH','MOBILE NO.'])
print(sd)

