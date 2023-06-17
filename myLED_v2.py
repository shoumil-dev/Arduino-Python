#Used to turn on the RGB LED to indicate the condition of the tank 
#Created By : Shoumil Guha (MC03)
#Created Date: 17/5/2022
#Version = '1.0'
from pymata4 import pymata4
import time

#inputs are: PYMATA4 Arduino, INT pin numbers for respective colors, STRING conditions for IF statements
def statusLED(myArduino, red, green, blue, condition):

    #Setting PWM pins to corresponding colours/hues of the LED
    myArduino.set_pin_mode_pwm_output(red)
    myArduino.set_pin_mode_pwm_output(green)
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
    
    if condition == "LOW":
        printColour("yellow", False)
    if condition == "NEAR EMPTY":
        printColour("red", False)
    if condition == "HIGH":
        printColour("yellow", False)
    if condition == "NEAR FULL":
        printColour("red", False)
    if condition == "MAXIMUM":
        printColour("blue", False)
        #print("TANK IS AT MAXIMUM CAPACITY")
    if condition == "RAPID CHANGE":
        printColour("yellow", True)
        #print("Rapid Change in Volume Detected!")
    if condition == "OFF":
        setColour("off")
