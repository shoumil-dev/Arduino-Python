from pymata4 import pymata4
import time

myArduino = pymata4.Pymata4()
green = 3
red = 5
blue = 11

myArduino.set_pin_mode_pwm_output(green)
myArduino.set_pin_mode_pwm_output(red)
myArduino.set_pin_mode_pwm_output(blue)

def setColor(setColor):
    rgbValues = colors[setColor]
    myArduino.pwm_write(red, rgbValues[0])
    myArduino.pwm_write(green, rgbValues[1])
    myArduino.pwm_write(blue, rgbValues[2])

def printColor(colour, blink):
    setColor(colour)
    
    if blink:
        time.sleep(0.5)
        setColor("off")
        time.sleep(0.5)

colors = {
    "off" : [0,0,0],
    "red" : [255,0,0],
    "green" : [0,255,0],
    "blue" : [0,0,255],
    "yellow" : [255,80,0]
}

while True:
    try:
        nearEmpty = False
        nearFull = False
        highVol = False
        lowVol = False
        overFull = True
        extendedEmpty = False
        extendedFull = False
        rapidChange = False
        
        if nearEmpty or nearFull:
            printColor("red", False)
        elif highVol or lowVol:
            printColor("yellow", False)
        elif extendedEmpty or extendedFull:
            printColor("red", True)
        elif overFull:
            printColor("blue", False)
        elif rapidChange:
            printColor("yellow", True)

    except KeyboardInterrupt:
        print("Shutting down...")
        setColor("off")
        myArduino.shutdown()
        exit(0)