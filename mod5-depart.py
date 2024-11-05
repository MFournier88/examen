import busio
import board
import time
import pigpio
import sys

from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.ads1115 import P0
from adafruit_ads1x15.analog_in import AnalogIn

# Init ADS1115
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c,2/3)
data = AnalogIn(ads, P0)

# Init GPIO
pi = pigpio.pi()
R = 26
G = 19
B = 13
BTN = 6
pi.set_mode(R,pigpio.OUTPUT)
pi.set_mode(G,pigpio.OUTPUT)
pi.set_mode(B,pigpio.OUTPUT)
pi.write(R,0)
pi.write(G,0)
pi.write(B,0)
cur = pi.read(BTN)
last = cur
compteur = 0
count = 0
isPressed = False
LED = R
isAllume = True
# Test
while True:
    try:
        print(data.value, data.voltage)
        cur = pi.read(BTN)
        if(not isPressed):
            if(cur == 1):
                count = 0
            elif(count < 4):
                count += 1
            elif(count == 4):
                
                count = 0
                isPressed = True
        else:
            if(cur == 0):
                count = 0
            elif(count < 4):
                count += 1
            elif(count == 4):
                count +=1
                isPressed = False

       

        last = cur
        
        

    except KeyboardInterrupt:
        pi.write(R,0)
        pi.write(G,0)
        pi.write(B,0)
        sys.exit()

            
