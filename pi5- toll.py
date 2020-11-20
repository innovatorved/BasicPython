from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)

data=[['UP41D2002','VED GUPTA','HV',1010],['UP32J2332','JAYA TRIPATHI','LV',1010],['UP32J2232','VIKRAL SINGH','HV',1788]]
hv=300
lv=200
amount=0

def deld():
    del(data[x][3])
    data[x].append(r)
    print('Available balance is: ',data[x][3])

while True:
    GPIO.output(36,GPIO.LOW)
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
                        GPIO.output(36,GPIO.HIGH)
                    else:
                        r=data[x][3]-hv
                        amount+=100
                        deld()
                        GPIO.output(40,GPIO.HIGH)
                        GPIO.output(38,GPIO.LOW)
                        sleep(2)
                        GPIO.output(40,GPIO.LOW)
                        GPIO.output(38,GPIO.HIGH)
                        sleep(2)
                        GPIO.output(40,GPIO.LOW)
                        GPIO.output(38,GPIO.LOW)
                        
                elif data[x][2]=='LV':
                    if data[x][3]<lv:
                        print('BALANCE LOW')
                        print('balance is: ',data[x][3])
                        GPIO.output(36,GPIO.HIGH)

                    else:
                        r=data[x][3]-lv
                        amount+=200
                        deld()
                        GPIO.output(40,GPIO.HIGH)
                        GPIO.output(38,GPIO.LOW)
                        sleep(2)
                        GPIO.output(40,GPIO.LOW)
                        GPIO.output(38,GPIO.HIGH)
                        sleep(2)
                        GPIO.output(40,GPIO.LOW)
                        GPIO.output(38,GPIO.LOW)
                        

        print('Government balance: ',amount)
                    
            
                
    
