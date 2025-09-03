import RPi.GPIO as GPIO
import time
#importing modules that we will use in the program
5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#more setup

#preparing specific GPIO pins for output
GPIO.setup(26, GPIO.OUT) #setting up the green LED
GPIO.setup(5, GPIO.OUT) #setting up the yellow LED
GPIO.setup(22, GPIO.OUT) #setting up the red LED
while True:
    print('GREEN ON') #message to the console
    GPIO.output(26, GPIO.HIGH) #activates the green LED
    time.sleep(5) #waits 5 seconds
    print("GREEN OFF")
    GPIO.output(26, GPIO.LOW)
    print('YELLOW ON')
    GPIO.output(5, GPIO.HIGH) # activates the yellow LED
    time.sleep(1) #waits for 1 second
    print("YELLOW OFF")
    GPIO.output(5, GPIO.LOW)
    print('RED ON')
    GPIO.output(22, GPIO.HIGH) #turns on the LED
    time.sleep(4) #waits for 4 seconds
    print("RED OFF")
    GPIO.output(22, GPIO.LOW)
    