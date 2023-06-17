from logging import exception
import time
from pymata4 import pymata4

triggerpin = 11
echo_pin = 12

board = pymata4.Pymata4()

def the_callback(data):
    print(data)

board.set_pin_mode_sonar(triggerpin, echo_pin, the_callback)

while True:
    try:
        time.sleep(0.1)
        board.sonar_read(triggerpin)
    except Exception:
        board.shutdown()