#Used to turn on the RGB LED to indicate the condition of the tank 
#Created By : Shoumil Guha (MC03)
#Created Date: 6/5/2022
#Version = '1.0'
from pymata4 import pymata4
import time

myArduino = pymata4.Pymata4()
green = 3
red = 5
blue = 11

myArduino.set_pin_mode_pwm_output(green)
myArduino.set_pin_mode_pwm_output(red)
myArduino.set_pin_mode_pwm_output(blue)

#Used to set the RGB values of the LED
def setColour(setColour):
    rgbValues = colours[setColour]
    myArduino.pwm_write(red, rgbValues[0])
    myArduino.pwm_write(green, rgbValues[1])
    myArduino.pwm_write(blue, rgbValues[2])

#Used to call to write to the LED pins & if LED should blink
def printColour(colour, blink):
    setColour(colour)
    
    if blink:
        time.sleep(1)
        setColour("off")
        time.sleep(1)

#Predefined RGB values for the LED
colours = {
    "off" : [0,0,0],
    "red" : [255,0,0],
    "green" : [0,255,0],
    "blue" : [0,0,255],
    "yellow" : [255,80,0]
}

#To test the LED code
while True:
    try:
        #Test conditions
        #condition = "LOW"
        #condition = "NEAR EMPTY"
        #condition = "HIGH"
        #condition = "NEAR FULL"
        condition = "MAXIMUM"
        #condition = "RAPID CHANGE" #Test Value

        if condition == "LOW":
            printColour("yellow", False)
        if condition == "NEAR EMPTY":
            printColour("red", False)
        if condition == "HIGH":
            printColour("yellow", False)
        if condition == "NEAR FULL":
            printColour("red", False)
        if condition == "MAXIMUM":
            printColour("green", False)
            #print("TANK IS AT MAXIMUM CAPACITY")
        if condition == "RAPID CHANGE":
            printColour("green", True)
            #print("Rapid Change in Volume Detected!")
        if condition == "OFF":
            direction = 0

    except KeyboardInterrupt:
        print("Shutting down...")
        setColour("off")
        myArduino.shutdown()
        exit(0)