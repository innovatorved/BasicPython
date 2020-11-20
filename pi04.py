import picamera
from time import sleep
from RPi import GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(40,GPIO.OUT)
while True:
    a=GPIO.input(40)
    sleep(0.50)
    print(a)
    if a==1:
        camera=picamera.PiCamera()
        camera.start_preview()
        sleep(1)
        camera.capture('img01.jpg')
        sleep(1)
        camera.stop_preview()
        camera.close()
        print('Done')
    

