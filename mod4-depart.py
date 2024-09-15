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
ads = ADS1115(i2c)
data = AnalogIn(ads, P0)

# Init GPIO
pi = pigpio.pi()
R = 26
G = 19
B = 13
pi.set_mode(R,pigpio.OUTPUT)
pi.set_mode(G,pigpio.OUTPUT)
pi.set_mode(B,pigpio.OUTPUT)
pi.write(R,0)
pi.write(G,0)
pi.write(B,0)

# Test
while True:
    try:
        print(data.value, data.voltage)
        pi.write(R,1)
        pi.write(G,0)
        pi.write(B,0)
        time.sleep(1)
        
        pi.write(R,0)
        pi.write(G,1)
        pi.write(B,0)
        time.sleep(1)
        
        pi.write(R,0)
        pi.write(G,0)
        pi.write(B,1)
        time.sleep(1)

    except KeyboardInterrupt:
        pi.write(R,0)
        pi.write(G,0)
        pi.write(B,0)
        sys.exit()
