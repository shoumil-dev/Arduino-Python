import time

from pymata4 import pymata4

# some globals
digitalOutput = 10 # output LED
digitalInput = 6 # input wire


#create board
myArduino = pymata4.Pymata4()

#set pin states
myArduino.set_pin_mode_digital_output(digitalOutput)
myArduino.set_pin_mode_digital_input(digitalInput)

#use KeyboardInterrupt to make it exitable
try:
    while True:
        #read in value
        value = myArduino.digital_read(digitalInput)
        #write it back out again
        myArduino.digital_write(digitalOutput,0)
        #wait for a bit
        time.sleep(0.0000001)
        print (value)
        if value[0] == 0:
            myArduino.digital_pin_write(digitalOutput,1)



except KeyboardInterrupt:
    #Cleanup
    myArduino.shutdown()
