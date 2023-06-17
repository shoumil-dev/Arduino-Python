from pymata4 import pymata4
import time
myArduino = pymata4.Pymata4()
charLookup = {
        "0" : "11111100",
        "1" : "01100000", 
        "2" : "11011010",
        "3" : "11110010", 
        "4" : "01100110", 
        "5" : "10110110", 
        "6" : "10111110", 
        "7" : "11100000", 
        "8" : "11111110", 
        "9" : "11110110", 
        "A" : "11101110", 
        "B" : "00111110", 
        "C" : "00101010", 
        "D" : "00111010", 
        "E" : "11001110",
        "F" : "11100110", 
        "G" : "00001010", 
        "H" : "10110110", 
        "I" : "00011110", 
        "J" : "00111000", 
        "K" : "00111000", 
        "L" : "01101110", 
        "N" : "01110110", 
        "O" : "11011010", 
        "P" : "11111100", 
        "Q" : "01100000", 
        "R" : "11011010",
        "S" : "11110010",
        "T" : "01100110",
        "U" : "10110110",
        "V" : "10111110",
        "X" : "11100000",
        "U" : "11111110",
        "Z" : "11110110",
        "." : "00000001",
        " " : "00000000"
    }

def string_determiner(character,index):
    displayData = charLookup[character]
    segmentValue = displayData[index]
    return int(segmentValue)


displayCharc = input("What to display?\n")
while displayCharc not in charLookup:
    print("Can't Display That")
    displayCharc = input("What to display?\n")


myArduino.set_pin_mode_digital_output(2)
myArduino.set_pin_mode_digital_output(3)
myArduino.set_pin_mode_digital_output(4)
myArduino.set_pin_mode_digital_output(5)
myArduino.set_pin_mode_digital_output(6)
myArduino.set_pin_mode_digital_output(7)
myArduino.set_pin_mode_digital_output(8)
myArduino.set_pin_mode_digital_output(9)
#myArduino.set_pin_mode_digital_output()
pinOut = [2,3,4,5,6,7,8,9,10]
d1 = 9
d2 = 10
# d2 = 4 not needed for 1 segment
# d3 = 3 not needed for 1 segment
# d4 = 2 not needed for 1 segment

try:
    while True:
        seg = 0
        for x in pinOut:
            myArduino.digital_write(d1,0)
            myArduino.digital_write(x,string_determiner(displayCharc,seg))
            seg +=1
            time.sleep(0.01)

        
        myArduino.digital_pin_write(D,0)

except KeyboardInterrupt:
    myArduino.shutdown()
