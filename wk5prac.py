from pymata4 import pymata4
import time
#from lightingDeclarations import lighting
board = pymata4.Pymata4()
print("Connection Established!")

#Setup pins
board.set_pin_mode_digital_output(10)
board.set_pin_mode_digital_input(6)
board.digital_pin_write(10,1)
while True:
    time.sleep(0.1)

    

    buttonValue, time_stamp = board.digital_read(6)
    print(buttonValue)
    if buttonValue == 1:
        board.digital_pin_write(10,0)