import machine
import time

led_pin = machine.Pin(23, machine.Pin.OUT)
#pin2 = machine.Pin(22,machine.Pin.OUT)
boton = machine.Pin(21, machine.Pin.IN)
led_pin.value(0)
print("asdjasdkljasl",boton.value())
while True:
    val = boton.value()
    print("VAL ANTES",val)
    time.sleep(1)
    if val:
        print("VAL DP",val)
        led_pin.value(1)
        print("LED ON")
        time.sleep(2)
    else:
        led_pin.value(0)
        #if not val:
        #    led_pin.value(0)
        #    print("LED OFF")
        #    time.sleep(2)
    #led_pin.value(0)
