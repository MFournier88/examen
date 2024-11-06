import pigpio
import time

LED = 26
MAX = 255 # La valeur maximale que set_PWM_dutycycle() accepte
pi = pigpio.pi()
pi.set_mode(LED,pigpio.OUTPUT)
cycle = 0 # Variable qui correspond à l'intensité (simulée) du voltage

try:
    while cycle < MAX:
        cycle += 1
        pi.set_PWM_dutycycle(LED,cycle)
        time.sleep(0.01)
    pi.write(LED,0)
    
except KeyboardInterrupt:
    pi.write(LED,0)
