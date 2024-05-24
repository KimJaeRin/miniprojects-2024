# DHT11_test.py
import adafruit_dht
import time
import RPi.GPIO as GPIO
import board


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
dhtDevice = adafruit_dht.DHT11(board.D18)

while (True):
    try:
        temp = dhtDevice.temperature
        humid = dhtDevice.humidity
        print(f'Temp : {temp}C / Humid : {humid}%')
        time.sleep(2)
    except RuntimeError as ex:
        print(ex.args[0])
    except KeyboardInterrupt as ex:
        break

dhtDevice.exit()