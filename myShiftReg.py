from pymata4 import pymata4
import time

#defining arduino
myArduino = pymata4.Pymata4()

#character table
charLookup = {
    "A" : "1110111",
    "B" : "0011111",
    "C" : "1001110",
    "D" : "0111101",
    "E" : "1001111",
    "F" : "1000111",
    "G" : "1011110",
    "H" : "0010111",
    "I" : "1010000",
    "J" : "1011000",
    "K" : "0110111",
    "L" : "0110000",
    "M" : "",
    "N" : "0010101",
    "O" : "0011101",
    "P" : "1100111",
    "Q" : "1110011",
    "R" : "0000101",
    "S" : "1011011",
    "T" : "0001111",
    "U" : "0111110",
    "V" : "0011100",
    "W" : "",
    "X" : "",
    "Y" : "0111011",
    "Z" : "1101101",

    "1" : "0110000",
    "2" : "1101101",
    "3" : "1111001",
    "4" : "0110011",
    "5" : "1011011",
    "6" : "1011111",
    "7" : "1110000",
    "8" : "1111111",
    "9" : "1111011",
    "0" : "1111110",
    "" : "0000000",
}

#mapping 7seg to microcontroller pins
D1 = 13
D2 = 12
D3 = 11
D4 = 10
dataLine = 7
outputClock = 6
inputClock = 5
SRCLR = 4
OE = 3

#keeping pins in a list
# segments = [A,B,C,D,E,F,G]
commons = [D1, D2, D3, D4]

#initialising pins as output
myArduino.set_pin_mode_digital_output(D4)
myArduino.set_pin_mode_digital_output(D3)
myArduino.set_pin_mode_digital_output(D2)
myArduino.set_pin_mode_digital_output(D1)
myArduino.set_pin_mode_digital_output(dataLine)
myArduino.set_pin_mode_digital_output(outputClock)
myArduino.set_pin_mode_digital_output(inputClock)
myArduino.set_pin_mode_digital_output(SRCLR)
myArduino.set_pin_mode_digital_output(OE)

myArduino.digital_write(SRCLR, 1)
myArduino.digital_write(OE, 0)

#turning on and off common pin function
def turnOn(position):
    myArduino.digital_write(commons[position], 0)

def turnOff(position):
    myArduino.digital_write(commons[position], 1)

def triggerInput(bit):
    myArduino.digital_write(dataLine, bit)
    myArduino.digital_write(inputClock, 0)
    myArduino.digital_write(inputClock, 1)
    myArduino.digital_write(inputClock, 0)

def triggerOutput():
    myArduino.digital_write(outputClock, 0)
    myArduino.digital_write(outputClock, 1)
    myArduino.digital_write(outputClock, 0)

def clear():
    myArduino.digital_write(dataLine, 0)
    for i in range(0,8):
        myArduino.digital_write(inputClock, 0)
        myArduino.digital_write(inputClock, 1)
        myArduino.digital_write(inputClock, 0)
    triggerOutput()

def dispLetter(letter, position):
    binary = charLookup[letter]
    binary = binary[::-1]
    
    for bit in binary: 
        bit = int(bit)
        triggerInput(bit)
    triggerOutput()
    turnOn(position)
    
    turnOff(position)
    
#lighting up a word
def lightUp(word):

    lenCommons = len(commons)
    for i in range(lenCommons):
        turnOff(i)
    
    length = len(word)
    for i in range(length):
        dispLetter(word[i], i)


#main
clear()
while True:
    try:
        lightUp("COCK")

    except KeyboardInterrupt:
        clear()
        print("Shutting down...")
        myArduino.shutdown()
        exit(0)
