from RPi import GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(3,OUT)

print('\nEnter ON for led on-')
print('Enter OFF for led off-')
a=input('Enter ur choice:')

if a=='ON' or 'on':
    GPIO.output(3,1)
    print('LED on')

elif a=='OFF' or 'off':
    GPIO.output(3,0)
    print('LED off')

else:

    print('Wrong Input')
