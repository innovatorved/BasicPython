from time import sleep
from RPi import GPIO

RS=36
RW=38
E=21

A=31
B=33
C=35
D=37

l=['A','B','C','D']

#alphabets
a=[[0,1,0,0],[0,0,0,1]]
b=[[0,1,0,0],[0,0,1,0]]
c=[[0,1,0,0],[0,0,1,1]]
d=[[0,1,0,0],[0,1,0,0]]
e=[[0,1,0,0],[0,1,0,1]]
f=[[0,1,0,0],[0,1,1,0]]
g=[[0,1,0,0],[0,1,1,1]]
h=[[0,1,0,0],[1,0,0,0]]
i=[[0,1,0,0],[1,0,0,1]]
j=[[0,1,0,0],[1,0,1,0]]
k=[[0,1,0,0],[1,0,1,1]]
l=[[0,1,0,0],[1,1,0,0]]
m=[[0,1,0,0],[1,1,0,1]]
n=[[0,1,0,0],[1,1,1,0]]
o=[[0,1,0,0],[1,1,1,1]]
p=[[0,1,0,1],[0,0,0,0]]
q=[[0,1,0,1],[0,0,0,1]]
r=[[0,1,0,1],[0,0,1,0]]
s=[[0,1,0,1],[0,0,1,1]]
t=[[0,1,0,1],[0,1,0,0]]
u=[[0,1,0,1],[0,1,0,1]]
v=[[0,1,0,1],[0,1,1,0]]
w=[[0,1,0,1],[0,1,1,1]]
x=[[0,1,0,1],[1,0,0,0]]
y=[[0,1,0,1],[1,0,0,1]]
z=[[0,1,0,1],[1,0,1,0]]

#cmd
fo_bit=[[0,0,1,0],[1,0,0,0]]    #four bit mode
clear=[[0,0,0,0],[0,0,0,1]]     #clear screen
home=[[0,0,0,0],[0,0,1,0]]      #return home
cur_of=[[0,0,0,0],[1,1,0,0]]    #cursor of
cur_on=[[0,0,0,0],[1,1,1,0]]    #cursor on
first=[[1,0,0,0],[0,0,0,0]]         #for first line
secound=[[1,1,0,0],[0,0,0,0]]          #second line


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(false)
GPIO.setup(RS,GPIO.OUT)
GPIO.setup(RW,GPIO.OUT)
GPIO.setup(E,GPIO.OUT)
GPIO.setup(a,GPIO.OUT)
GPIO.setup(b,GPIO.OUT)
GPIO.setup(c,GPIO.OUT)
GPIO.setup(d,GPIO.OUT)

def data(g):
    GPIO.output(RS,1)
    GPIO.output(RW,0)
    for x in range(0,len(g),1):
        GPIO.output(l[x],g[0][x])
    
    GPIO.output(E,1)
    sleep(0.010)
    GPIO.output(E,0)
    sleep(0.010)
    
    for x in range(0,len(g),1):
        GPIO.output(l[x],g[1][x])

    GPIO.output(E,1)
    sleep(0.010)
    GPIO.output(E,0)
    sleep(0.010)

def cmd(g):
    GPIO.output(RS,0)
    GPIO.output(RW,0)
    for x in range(0,len(g),1):
        GPIO.output(l[x],g[0][x])
    
    GPIO.output(E,1)
    sleep(0.010)
    GPIO.output(E,0)
    sleep(0.010)
    
    for x in range(0,len(g),1):
        GPIO.output(l[x],g[1][x])

    GPIO.output(E,1)
    sleep(0.010)
    GPIO.output(E,0)
    sleep(0.010)


def set():
    cmd(fo_bit)
    cmd(clear)
    cmd(home)
    cmd(cur_on)
    cmd(first)


while True:
    set()
    aa=[]
    
    aa.append(input('print word on lcd: '))
    for x in range(0,len(aa[0]),1):
        data(x)
    
