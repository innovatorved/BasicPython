from EmulatorGUI import GPIO
import traceback
#import RPi.GPIO as GPIO
import time
def Main():
    try:
#====================================================
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(2, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(21, GPIO.IN)
        while(True):
                a = GPIO.input(21)
                if a==GPIO.HIGH:
                    GPIO.output(2,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(2,GPIO.LOW)
                    GPIO.output(3,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(3,GPIO.LOW)
                    GPIO.output(4,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(4,GPIO.LOW)
                    GPIO.output(5,GPIO.HIGH)
                    time.sleep(0.5)
                    GPIO.output(5,GPIO.LOW)
#=====================================================
    except Exception as ex:
        traceback.print_exc()
Main()
