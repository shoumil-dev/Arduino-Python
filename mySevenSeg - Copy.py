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
A = 9
B = 8
C = 7
D = 6
E = 5
F = 4
G = 3

#keeping pins in a list
segments = [A,B,C,D,E,F,G]
commons = [D1, D2, D3, D4]

#initialising pins as output
myArduino.set_pin_mode_digital_output(G)
myArduino.set_pin_mode_digital_output(F)
myArduino.set_pin_mode_digital_output(E)
myArduino.set_pin_mode_digital_output(D)
myArduino.set_pin_mode_digital_output(C)
myArduino.set_pin_mode_digital_output(B)
myArduino.set_pin_mode_digital_output(A)
myArduino.set_pin_mode_digital_output(D4)
myArduino.set_pin_mode_digital_output(D3)
myArduino.set_pin_mode_digital_output(D2)
myArduino.set_pin_mode_digital_output(D1)

#turning on and off common pin function
def turnOn(position):
    myArduino.digital_write(commons[position], 0)

def turnOff(position):
    myArduino.digital_write(commons[position], 1)

#lighting up a single letter
def dispLetter(letter, position):
    binary = charLookup[letter]
    for j in range(10):
        for i in range(len(binary)):
            segment = segments[i]
            state = int(binary[i])
            myArduino.digital_write(segments[i], state)
    
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
while True:
    try:
        lightUp("NUTS")

    except KeyboardInterrupt:
        print("Shutting down...")
        myArduino.shutdown()
        exit(0)