# main.py -- put your code here!

import machine
import time

led_pin = machine.Pin(23, machine.Pin.OUT)
pin2 = machine.Pin(22,machine.Pin.OUT)
boton = machine.Pin(17, machine.Pin.IN)
state = 0
while True:
    val = boton.value()

    if val:
        if state == 0:
            state = 1
        else:
            state = 0
    if state == 1:
        led_pin.value(1)
        pin2.value(0)
        print("LED ON")
    else:    state == 0:
        led_pin.value(0)
        pin2.value(1)
    
        
    # led_pin.value(1)
    # pin2.value(1)
    # print("LED ON")
    # time.sleep(1)
    # led_pin.value(0)
    # pin2.value(0)
    # print("LED OFF")
    # time.sleep(1)

