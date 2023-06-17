import time
from pymata4 import pymata4

from myLED_v2 import statusLED

myArduino = pymata4.Pymata4()
red = 9
green = 10
blue = 11



while True:
        try:
            #Test conditions
            #condition = "LOW"
            #condition = "NEAR EMPTY"
            #condition = "HIGH"
            #condition = "NEAR FULL"
            #condition = "MAXIMUM"
            condition = "RAPID CHANGE" #Test Value
            statusLED(myArduino, red, green, blue, "MAXIMUM")
            

        except KeyboardInterrupt:
            print("Shutting down...")
            statusLED(myArduino, red, green, blue, "OFF")
            myArduino.shutdown()
            exit(0)