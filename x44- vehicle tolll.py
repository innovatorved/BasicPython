data=[['UP41D2002','VED GUPTA','HV',2010],['UP32J2332','JAYA TRIPATHI','LV',1010],['UP32J2232','VIKRAL SINGH','HV',1788]]
hv=100
lv=200
amount=0

def deld():
    del(data[x][3])
    data[x].append(r)
    print('Available balance is: ',data[x][3])

while True:
    a=input('\nscan pls: ')
    if a=='add':
        print('enternthe vehicle info- ')
        b=input('Enter vehicle number: ')
        c=input('Name of Owner: ')
        d=input('Vehicle type HV or LV: ')
        e=int(input('Enter account detail: '))
        dd=[b,c,d,e]
        data.append(dd)
        print('data successfully add!\n')

    else:
        for x in range(0,len(data),1):
            if a in data[x]:
                print('Name: ',data[x][1])
                print('Vehicle no.: ',data[x][0])
                print('vehicle type: ',data[x][2])
                print('Amount available: ',data[x][3])
                if data[x][2]=='HV':
                    if data[x][3]<hv:
                        print('BALANCE LOW')
                        print('balance is: ',data[x][3])
                        
                    else:
                        r=data[x][3]-hv
                        amount+=100
                        deld()
                elif data[x][2]=='LV':
                    if data[x][3]<lv:
                        print('BALANCE LOW')
                        print('balance is: ',data[x][3])

                    else:
                        r=data[x][3]-lv
                        amount+=200
                        deld()

        print('Government balance: ',amount)
                    
            
                
    
