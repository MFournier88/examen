import pigpio
import time

## Config --NE PAS MODIFIER--   ------------
pi = pigpio.pi()        
BTN = 6
cur = pi.read(BTN)
last = cur
count = 0
isPressed = False
##-------------------


compteur = 0

while True:
    try:
        cur = pi.read(BTN)
        if(not isPressed):
            if(cur == 1):
                count = 0
            elif(count < 4):
                count += 1
            elif(count == 4):
                count = 0
                isPressed = True
                # Permet de compter vous pouvez retirer
                #  si vous ne comptez pas
                compteur += 1
                print("J'ai appuyé ", compteur, ' fois')
                # -----------------------------------
                #Mettre le code à effecter sur un clic ici
                #

                #------------------------------------
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
        break

            
