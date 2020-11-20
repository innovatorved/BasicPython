from RPi import GPIO
from time import sleep
data=[['apple',95],['banana',40],['grapes',55],['papaya',80],['orange',60],['date',120],['pine apple',130]]
name=[data[0][0],data[1][0],data[2][0],data[3][0],data[4][0],data[5][0],data[0][0]]
count=0
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
while True:
    a= input('\nScan: ')
    if a=='ad_d':
        count=0
        b=input('Enter product name: ')
        c=int(input('MRP: '))
        GPIO.output(33,1)
        d=[b,c]
        data.append(d)
        name.append(b)
        print('data succesfully saved!')
        sleep(0.50)
        GPIO.output(33,0)
        
    elif a=='x':
        count=0
        print('RESET')
    else:
        for x in range(0,len(data),1):
            if a in data[x]:
                print('product available')
                GPIO.output(35,1)
                print(a,':',data[x][1],'ruppes')
                count+=data[x][1]
                sleep(1)
                GPIO.output(35,0)
        if a not in name:
            GPIO.output(37,1)
            print('not available\n')
            sleep(1)
            GPIO.output(37,0)
        print('total: ',count,'rupees')
