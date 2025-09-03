import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
while True:
    while (GPIO.input(4) == 0):
        print('GREEN ON')
        GPIO.output(19, GPIO.HIGH)
        time.sleep(5)
        print('GREEN OFF')
        GPIO.output(19, GPIO.LOW)
        print('YELLOW ON')
        GPIO.output(5, GPIO.HIGH)
        time.sleep(1)
        print('YELLOW OFF')
        GPIO.output(5, GPIO.LOW)
        print('RED ON')
        GPIO.output(22, GPIO.HIGH)
        time.sleep(4)
        print('RED OFF')
        GPIO.output(22, GPIO.LOW)
    else:
        GPIO.output(19, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(22, GPIO.LOW) 