from RPi import GPIO as power
from time import sleep as stop

a=29
b=31
c=33
d=35
e=37
f=40
g=38
seg=[a,b,c,d,e,f,g]

power.setmode(power.BOARD)
power.setwarnings(False)
power.setup(a,power.OUT)
power.setup(b,power.OUT)
power.setup(c,power.OUT)
power.setup(d,power.OUT)
power.setup(e,power.OUT)
power.setup(f,power.OUT)
power.setup(g,power.OUT)

zero=[1,1,1,1,1,1,0]
one=[0,1,1,0,0,0,0]
two=[1,1,0,1,0,0,1]
three=[1,1,1,1,0,0,1]
four=[0,1,1,0,0,1,1]
five=[1,0,1,1,0,1,1]
six=[1,0,1,1,1,1,1]
seven=[1,1,1,0,0,0,0]
eight=[1,1,1,1,1,1,1]

num=[zero,one,two,three,four,five,six,seven,eight]
while  True:
    for x in range(0,len(num),1):
        power.output(seg,num[x])
        stop(2)
