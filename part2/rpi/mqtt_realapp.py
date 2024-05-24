# mqtt_realapp.py
# 온습도센서 데이터 통신, RGB LED Setting
#MQTT -> json transfer

import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import adafruit_dht
import board
import time
import datetime as dt
import json

red_pin = 4
green_pin = 6
dht_pin = 18

dev_id = 'PKNU_77'
loop_num = 0

## 초기화 시작

def onConnect(client, userdata, flags, reason_code, properties):
    print(f'연결성공 : {reason_code}')
    client.subscribe('pknu/rcv')

def onMessage(client, userdata, msg):
    print(f'{msg.topic} + {msg.payload}')

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(dht_pin, GPIO.IN) # 온습도값을 RPi에서 받는것
dhtDevice = adafruit_dht.DHT11(board.D18)

## 초기화 끝

## 실행 시작

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = onConnect
mqttc.on_message = onMessage

# 192.168.5.2 window ip
mqttc.connect('192.168.5.2', 1883, 60)

mqttc.loop_start()
while True:
    time.sleep(2)
    try:

        # 온습도 값 받아서 MQTT로 전송
        temp = dhtDevice.temperature
        humd =dhtDevice.humidity
        print(f'{loop_num} - temp:{temp}/humid:{humd}')

        origin_data = { 'DEV_ID' : dev_id,
                        'CURR_DT' : dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'TYPE' : 'TEMPHUMID', 
                        'VALUE' : f'{temp}|{humd}'
                        }
        pub_data = json.dumps(origin_data, ensure_ascii=False)

        mqttc.publish('PKNU/data/', pub_data)
        loop_num += 1
    except RuntimeError as ex:
        print(ex.args[0])
    except KeyboardInterrupt:
        break

mqttc.loop_stop()
dhtDevice.exit()
## 실행 끝