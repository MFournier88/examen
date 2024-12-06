import board
import busio
from time import sleep
from adafruit_ht16k33 import matrix
import pigpio
from random import randint

servo = 21 # Le numéro GPIO de la broche ou est connecté le servomoteur
FREQ = 50 # Fréquence en Hz de la période

pi = pigpio.pi()
pi.set_mode(servo,pigpio.OUTPUT)
pi.set_PWM_frequency(servo,FREQ)
pi.set_PWM_range(servo,100) # Valeurs possibles dutycycle de 0-100

i2c = busio.I2C(board.SCL, board.SDA)
mat = matrix.Matrix8x8(i2c)

## NE PAS MODIFIER CE QUI EST CI-DESSUS!! N'utilisez pas d'autre GPIO que le 21
while True:
    print(randint(0,10))
    sleep(0.5)
