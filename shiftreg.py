# Solutions and skeleton code for driving ENG1013 Project Seven (8) Segment Display
# Written by James Salamy Apr 2022
# Check for TODO markings in code (can find with cmd f), to finish/understand the process

# #imports
# import time
# from pymata4 import pymata4

# #segment pins: (/)
# # D1=13
# # A=12
# # F=11
# # D2=10
# # D3=9
# # B=8
# # #spacing for organisation.
# # E=7
# # D=6
# # dec=5
# # C=4
# # G=3
# # D4=2
# # TODO: finish this list (/)
# segPins = [D1,A,F,D2,D3,B,E,D,dec,C,G,D4]
# #global lookup table
# charLookup = {
#         "0" : int("11111100",2), #1111 - on 0000 - off
#         "1" : int("01100000",2),
#         "2" : int("11011010",2),
#         "3" : int("11110010",2),
#         "4" : int("01100110",2),
#         "5" : int("10110110",2),
#         "6" : int("10111110",2),
#         "7" : int("11100000",2),
#         "8" : int("11111110",2),
#         "9" : int("11110110",2),
#         "A" : int("11101110",2),
#         "B" : int("00111110",2),
#         "C" : int("00011010",2),
#         "D" : int("01111010",2),
#         "E" : int("10011110",2),
#         "F" : int("10001110",2),
#         "G" : int("11110110",2),
#         "H" : int("00101110",2),
#         "I" : int("01100000",2),
#         "J" : int("01110000",2),
#         "K" : int("00000000",2),
#         "L" : int("00011100",2),
#         "M" : int("00101010",2),
#         "N" : int("00101010",2),
#         "O" : int("00111010",2),
#         "P" : int("11001110",2),
#         "Q" : int("11100110",2),
#         "R" : int("00001010",2),
#         "S" : int("10110110",2),  
#         "T" : int("00000000",2),
#         "U" : int("00111000",2),
#         "V" : int("00000000",2),
#         "W" : int("00111000",2),
#         "X" : int("00000000",2),
#         "Y" : int("01110110",2),
#         "Z" : int("11011010",2)
#     }

# def eight_string_2_output(stringToSeg):
#     #function to make codes from a string

#     #put all to upper case (only 1 case available on 7seg)
#     capString = stringToSeg.upper()

#     #cover unprintable characters
#     capString = capString.replace("M","NN")
#     capString = capString.replace("W","UU")
#     #TODO: which other characters do you need to cover?

#     segCodes = []
#     #check and process each character
#     for character in capString:
#         segCodes.append(charLookup[character])

#     #return list of codes
#     return segCodes

# def write_7_seg(board,segCode,digitPin):
#     # turn off the display
#     board.digital_write(digitPin,1)
#     #write segment states - note writing quickly is important
#     # set up a 'pin mask' to do element by element comparison:
#     pinMask = 0b10000000 #this is a binary representation of 8 individual numbers
#     #NB: computers process binary information very fast
#     for i in range(8):
#         #TODO if you don't understand this, add print statements to understand what
#         # & and >> are doing in this code
#         if (segCode) & pinMask >> i:
#             #if the 1 in pinMask, shifted to the left i=0,1,2,... places
#             #matches to a 1 in corresponding spot, then:
#             board.digital_write(segPins[i],1)
#             #turn segment on
#         else:
#             #turn segment off
#             board.digital_write(segPins[i],0)

#     #turn display back on
#     board.digital_write(digitPin,0)

#     time.sleep(0.1)
#     #end of function, no return value needed
#     return


# WEEK 7 CODE PROVIDED::::

import time

#TODO setup board and output pins
from pymata4 import pymata4

ardBoard=pymata4.Pymata4()

#segment pins: (/)
ser=2
rclk=3
srclk=4
D1=10
D2=11
D3=12
D4=13

# set pinmask
pinMask=0b00000001

# TODO: finish this list (/)
pins = [ser,srclk,D1,D2,D3,D4]


#TODO integrate the appropriate parts of your completed code from week 5 (shift register coding)
charLookup = {
        "0" : int("11111100",2), #1111 - on 0000 - off
        "1" : int("01100000",2),
        "2" : int("11011010",2),
        "3" : int("11110010",2),
        "4" : int("01100110",2),
        "5" : int("10110110",2),
        "6" : int("10111110",2),
        "7" : int("11100000",2),
        "8" : int("11111110",2),
        "9" : int("11110110",2),
        "A" : int("11101110",2),
        "B" : int("00111110",2),
        "C" : int("00011010",2),
        "D" : int("01111010",2),
        "E" : int("10011110",2),
        "F" : int("10001110",2),
        "G" : int("11110110",2),
        "H" : int("00101110",2),
        "I" : int("01100000",2),
        "J" : int("01110000",2),
        "K" : int("00000000",2),
        "L" : int("00011100",2),
        "M" : int("00101010",2),
        "N" : int("00101010",2),
        "O" : int("00111010",2),
        "P" : int("11001110",2),
        "Q" : int("11100110",2),
        "R" : int("00001010",2),
        "S" : int("10110110",2),  
        "T" : int("00000000",2),
        "U" : int("00111000",2),
        "V" : int("00000000",2),
        "W" : int("00111000",2),
        "X" : int("00000000",2),
        "Y" : int("01110110",2),
        "Z" : int("11011010",2)
    }

def eight_string_2_output(stringToSeg):
    #function to make codes from a string

    #put all to upper case (only 1 case available on 7seg)
    capString = stringToSeg.upper()

    #cover unprintable characters
    capString = capString.replace("M","NN")
    capString = capString.replace("W","UU")
    #TODO: which other characters do you need to cover?

    segCodes = []
    #check and process each character
    for character in capString:
        segCodes.append(charLookup[character])

    #return list of codes
    return segCodes



def write_to_7_seg_series(segCode,ardBoard,pins,pinMask,ID):
    #TODO this function needs to take an individual segCode (for a segment)
    # and write it to a single digit, using the shift register.

    #write value into register
    for i in range(8):
        #TODO compare this to the code from week 5, why do we use << not >>?
        if (segCode) & (pinMask << i):
            ardBoard.digital_write(pins[0],1)
        else:
            ardBoard.digital_write(pins[0],0)
        #clock handling:
        #setup
        ardBoard.digital_write(pins[1],1)
        #hold
        ardBoard.digital_write(pins[1],0)

    #TODO think about why these steps push to the SR output
    #is there anything else we need to do here to ensure the output is visible?
    #if required, how to do another clock cycle push from shift to storage register
    # ardBoard.digital_write(pins[1],1)
    # ardBoard.digital_write(pins[1],0)
    
    # enable output
    #TODO what other signal do we need to ensure is set properly?

    ardBoard.digital_write(ID,0)
    time.sleep(200e-6)
    #disable output
    ardBoard.digital_write(ID,1)

def write_to_4_digits_serial(segCodes,ardBoard,pins,wait):
    
    pinMask = 0b00000001

    #force all digits off prior to draw
    ardBoard.digital_write(pins[2],1)
    ardBoard.digital_write(pins[3],1)
    ardBoard.digital_write(pins[4],1)
    ardBoard.digital_write(pins[5],1)

    #preset clock position clock
    ardBoard.digital_write(pins[1],0)

    #TODO think about what other shift register pins I should set

    #iterate and draw
    for j in range(len(segCodes)):
        #TODO why would we need to use a while loop in this place?
        while(True):
            #digit 0:
            write_to_7_seg_series(segCodes[j],ardBoard,pins,pinMask,pins[2])
            #digit 1:
            #BONUS TODO: how would we now write to additional characters?
            write_to_7_seg_series(segCodes[j],ardBoard,pins,pinMask,pins[3])
            write_to_7_seg_series(segCodes[j],ardBoard,pins,pinMask,pins[4])
            write_to_7_seg_series(segCodes[j],ardBoard,pins,pinMask,pins[5])
            time.sleep(wait)

#TODO write a function that uses these complete functions, combined with the function you wrote
# two weeks ago to drive an output through the Shift Register to the 7 segment display
def print_on_7seg (word, ardBoard,pins,pinMask,wait):
    segCodes=eight_string_2_output(word)

    write_to_4_digits_serial(segCodes,ardBoard,pins,wait)


#TODO make sure you think about what steps I haven't provided for you

#TODO finally, which 74HC595 control pins in our application need to be connected to the microcontroller?
# testing

testChar="A"
wait=5

print_on_7seg(testChar,ardBoard,pins,pinMask,wait)