from RPi import GPIO as power
from time import sleep as rukja

a=29
b=31
c=33
d=35
power.setmode(power.BOARD)
power.setwarnings(False)
power.setup(a,power.OUT)
power.setup(b,power.OUT)
power.setup(c,power.OUT)
power.setup(d,power.OUT)


def zero():
    power.output(a,0)
    power.output(b,0)
    power.output(c,0)
    power.output(d,0)

def one():
    power.output(a,0)
    power.output(b,0)
    power.output(c,0)
    power.output(d,1)

def two():
    power.output(a,0)
    power.output(b,0)
    power.output(c,1)
    power.output(d,0)

def three():
    power.output(a,0)
    power.output(b,0)
    power.output(c,1)
    power.output(d,1)

def four():
    power.output(a,0)
    power.output(b,1)
    power.output(c,0)
    power.output(d,0)

def five():
    power.output(a,0)
    power.output(b,1)
    power.output(c,0)
    power.output(d,1)

def six():
    power.output(a,0)
    power.output(b,1)
    power.output(c,1)
    power.output(d,0)

def seven():
    power.output(a,0)
    power.output(b,1)
    power.output(c,1)
    power.output(d,1)

def eight():
    power.output(a,1)
    power.output(b,0)
    power.output(c,0)
    power.output(d,0)

def nine():
    power.output(a,1)
    power.output(b,0)
    power.output(c,0)
    power.output(d,1)

def ten():
    power.output(a,1)
    power.output(b,0)
    power.output(c,1)
    power.output(d,0)

def eleven():
    power.output(a,1)
    power.output(b,0)
    power.output(c,1)
    power.output(d,1)

def twelve():
    power.output(a,1)
    power.output(b,1)
    power.output(c,0)
    power.output(d,0)

def thirteen():
    power.output(a,1)
    power.output(b,1)
    power.output(c,0)
    power.output(d,1)

def fourteen():
    power.output(a,1)
    power.output(b,1)
    power.output(c,1)
    power.output(d,0)

def fifteen():
    power.output(a,1)
    power.output(b,1)
    power.output(c,1)
    power.output(d,1)
    
    
while True:
   zero()
   rukiye(1)

   one()
   rukiye(1)

   two()
   rukiye(1)

   three()
   rukiye(1)

   four()
   rukiye(1)

   five()
   rukiye(1)

   six()
   rukiye(1)

   seven()
   rukiye(1)

   eight()
   rukiye(1)

   nine()
   rukiye(1)

   ten()
   rukiye(1)

   eleven()
   rukiye(1)

   twelve()
   rukiye(1)

   thirteen()
   rukiye(1)

   fourteen()
   rukiye(1)

   fifteen()
   rukiye(1)
   
