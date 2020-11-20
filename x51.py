import requests
from time import sleep

read='https://api.thingspeak.com/channels/971673/feeds.json?api_key=UNHZR7MV7OP0F7GO&results='
write='https://api.thingspeak.com/update?api_key=U6ML9RCD9A7ER5K6&field1='

def total():
    a=requests.get(read+str(1))
    b=a.json()
    c=b['feeds'][0]['field1']
    for x in b['feeds']:
        e=x['entry_id']
    return(e)

def data():
    print('\nEntry id: ',x['entry_id'],'--\n\tName: ',x['field1'],'\n\tBranch: ',x['field2'],'\n\tRoll.no: ',x['field3'],'\n\tFathers Name: ',x['field4'])

while True:
    a=int(input('\nEnter 1 for student data add on website-\nEnter 2 checking recent add data-\nEnter 3 for find particular Student id- \nEnter 4 for check student data by Roll.No-\nEnter your choice: '))
    if a==1:
        b=(input('Enter the Name of Student: '))
        c=(input('Enter the branch of student: '))
        d=(input('Enter the Roll No. of Student: '))
        e=(input('Enter the fathers name of Student: '))
        f=requests.post(write+str(b)+'&field2='+str(c)+'&field3='+str(d)+'&field4='+str(e))
        g=f.json()
        while g==0:
            f=requests.post(write+str(b)+'&field2='+str(c)+'&field3='+str(d)+'&field4='+str(e))
            g=f.json()
        print('\nData added succesfully id: ',g)

    elif a==2:
        e=total()
        print('\nTotal data available: ',e)
        d=int(input('\nhow much last id u find: '))
        a=requests.get(read+str(d))
        b=a.json()
        c=b['feeds'][0]['field1']
        for x in b['feeds']:
            data()

    elif a==3:
        e=total()
        print('\nTotal data available: ',e)
        f=int(input('\t\tEnter the id: '))
        g=requests.get(read+str(e))
        h=g.json()
        i=h['feeds'][0]['field1']
        for x in h['feeds']:
            if int(x['entry_id'])==f:
                data()
    elif a==4:
        f=input('Enter the Roll.No: ')
        e=total()
        a=requests.get(read+str(e))
        b=a.json()
        c=b['feeds'][0]['field1']
        for x in b['feeds']:
            if f==x['field3']:
                data()
        
        
        

