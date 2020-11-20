from time import sleep
from RPi import GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
RS = 37
RW = 35
EN = 33
lcd = [18,22,24,26,32,36,38,40]
GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.OUT)
GPIO.setup(36,GPIO.OUT)
GPIO.setup(32,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.output(lcd,[0,0,0,0,0,0,0,0])
def int2bin(d):
    d0 = (d & 0b00000001)>>0
    d1 = (d & 0b00000010)>>1
    d2 = (d & 0b00000100)>>2
    d3 = (d & 0b00001000)>>3
    d4 = (d & 0b00010000)>>4
    d5 = (d & 0b00100000)>>5
    d6 = (d & 0b01000000)>>6
    d7 = (d & 0b10000000)>>7
    print([d7,d6,d5,d4,d3,d2,d1,d0])
    return([d7,d6,d5,d4,d3,d2,d1,d0])
def lcdcmd(cmd):
    b = int2bin(cmd)
    GPIO.output(RS,0)   #set RS
    GPIO.output(RW,0)   #set RW
    GPIO.output(lcd, b)#set data/command
    GPIO.output(EN,1)   #set EN =1
    sleep(.01)            #sleep(1)
    GPIO.output(EN,0)   #set EN =0
    sleep(.01)
def lcddat(dat):
    b = int2bin(ord(dat))
    GPIO.output(RS,1)   #set RS
    GPIO.output(RW,0)   #set RW
    GPIO.output(lcd, b)#set data/command
    GPIO.output(EN,1)   #set EN =1
    sleep(.001)            #sleep(1)
    GPIO.output(EN,0)   #set EN =0
    sleep(.001)
def lcd_print(data):
    for x in data:
        lcddat(x)   
lcdcmd(0x0c)
lcdcmd(0x38)
lcdcmd(0x01)
lcdcmd(0x80)
lcd_print('ABHISHEK KATIYAR')
lcdcmd(0xC0)
lcd_print('  RASPBERRY PI  ')


