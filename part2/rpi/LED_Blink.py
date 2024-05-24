# LED_Blink.py
# Red LED 점등

import  RPi.GPIO as GPIO
import time

# RGB LED 핀 번호 세팅
red_pin = 4
green_pin = 6
blue_pin = 5

GPIO.setmode(GPIO.BCM) # GPIO.BOARD(1~40)
GPIO.setup(red_pin, GPIO.OUT) #4번 PIN으로 출력
GPIO.setup(green_pin, GPIO.OUT) #6번 PIN으로 출력
GPIO.setup(blue_pin, GPIO.OUT) #5번 PIN으로 출력


try:        
    while (True):
        GPIO.output(red_pin, False)
        GPIO.output(green_pin, False)
        GPIO.output(blue_pin, False)
        time.sleep(0.5) #sec

        # GPIO.output(red_pin, False)
        # GPIO.output(green_pin, True)
        # GPIO.output(blue_pin, False)
        # time.sleep(0.5)
       
        # GPIO.output(red_pin, False)
        # GPIO.output(green_pin, False)
        # GPIO.output(blue_pin, True)
        # time.sleep(0.5)

        GPIO.output(red_pin, True)
        GPIO.output(green_pin, True)
        GPIO.output(blue_pin, True)
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()
