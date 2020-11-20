import requests
from time import sleep
read='https://api.thingspeak.com/channels/996010/feeds.json?api_key=RSUICU67W4B5TZSI&results='
write='https://api.thingspeak.com/update?api_key=EPU2OWU774639QOI&field1='

while True:
    a=int(input('\nEnter 1 for data add on website-\nEnter 2 for writing data from website-\nenter 3 for find particular id value- \nenter your choice: '))
    if a==1:
        b=(input('\nEnter the data which want to store: '))
        c=requests.post(write+str(b))
        d=c.json()
        while d==0:
            c=requests.post(write+str(b))
            d=c.json()
        print('id is: ',d)

    elif a==2:
        a=requests.get(read+str(1))
        b=a.json()
        c=b['feeds'][0]['field1']
        for x in b['feeds']:
            e=x['entry_id']
        print('Total id: ',e)
        d=int(input('\nhow much last id u find: '))
        a=requests.get(read+str(d))
        b=a.json()
        c=b['feeds'][0]['field1']
        for x in b['feeds']:
            print(x['entry_id'],':',x['field1'])

    elif a==3:
        a=requests.get(read+str(1))
        b=a.json()
        c=b['feeds'][0]['field1']
        for x in b['feeds']:
            e=x['entry_id']
        print('Total id: ',e)
        
        f=int(input('Enter the id: '))
        g=requests.get(read+str(e))
        h=g.json()
        i=h['feeds'][0]['field1']
        for x in h['feeds']:
            if int(x['entry_id'])==f:
                print(x['field1'])
            
        
        

