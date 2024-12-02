import pigpio
from time import sleep

servo = 21 # Le numéro GPIO de la broche ou est connecté le servomoteur
FREQ = 50 # Fréquence en Hz de la période

pi = pigpio.pi()
pi.set_mode(servo,pigpio.OUTPUT)
pi.set_PWM_frequency(servo,FREQ)
pi.set_PWM_range(servo,100) # Valeurs possibles dutycycle de 0-100

plus90 = 12.5
moins90 = 2.5

pi.set_PWM_dutycycle(servo,plus90)
sleep(1)
pi.set_PWM_dutycycle(servo,moins90)