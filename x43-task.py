from time import sleep
data=[['apple',95],['banana',40],['grapes',55],['papaya',80],['orange',60],['date',120],['pine apple',130]]
name=[data[0][0],data[1][0],data[2][0],data[3][0],data[4][0],data[5][0],data[0][0]]
count=0
while True:
    a= input('\nScan: ')
    if a=='ad_d':
        count=0
        b=input('Enter product name: ')
        c=int(input('MRP: '))
        d=[b,c]
        data.append(d)
        name.append(b)
        print('data succesfully saved!')
        
    elif a=='x':
        count=0
        print('RESET')
    else:
        for x in range(0,len(data),1):
            if a in data[x]:
                print('product available')
                print(a,':',data[x][1],'ruppes')
                count+=data[x][1]
        if a not in name:
            print('not available\n')
        print('total: ',count,'rupees')
