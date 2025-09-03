import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

while True:
    while GPIO.input(4) == 0:
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(22, GPIO.HIGH)
    else:
        GPIO.output(19, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)

