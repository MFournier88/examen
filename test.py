# test.py
# Connecter le module ADS1115 au Pi
# Connecter un module Keystudio LED à GPIO 26
import pigpio
import busio
import board
import time

from adafruit_ads1x15.ads1115 import ADS1115
from adafruit_ads1x15.ads1115 import P0
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS1115(i2c,2)
data = AnalogIn(ads, P0)

GPIO = 26
pi = pigpio.pi()
pi.set_mode(GPIO,pigpio.OUTPUT)

while True:
    print(data.value, data.voltage)
    pi.write(GPIO,1)
    time.sleep(0.5)
    pi.write(GPIO,0)
    time.sleep(0.5)
