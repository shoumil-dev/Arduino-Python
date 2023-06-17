from pymata4 import pymata4
import mySevenSeg

myArduino = pymata4.Pymata4()

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
decimal = 2

#keeping pins in a list
segments = [A,B,C,D,E,F,G]
commons = [D1, D2, D3, D4]

#initialising pins as output
myArduino.set_pin_mode_digital_output(decimal)
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

myState = "high"

def main():
    if myState == "high":
        mySevenSeg.lightUp("HIGH")

    if myState == "low":
        mySevenSeg.lightUp("LOW")

    if myState == "empty":
        mySevenSeg.lightUp("EPTY")

    else:
        mySevenSeg.lightUp("NONE")

#main
while True:
    try:
        main()

    except KeyboardInterrupt:
        print("Shutting down...")
        myArduino.shutdown()
        exit(0)