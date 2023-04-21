import machine
import time


pin_rojo = machine.Pin(23, machine.Pin.OUT)
pin_verde = machine.Pin(22, machine.Pin.OUT)
boton = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_DOWN)
pin_rojo.value(0)
pin_verde.value(0)

boton.value(0)
peso = 10
frutos_secos = ["mani", "nueces", "almendras"]
fruto = 0


while True:
    val = boton.value()
    print("boton", val)
    
    print(frutos_secos[fruto])
    if not val:
        pressed = True
        pin_rojo.value(1)
        print("hola")
        time.sleep(1)
        fruto += 1
        if fruto == 3:
            fruto = 0
        boton.value(0)
    time.sleep(1)

    # if peso <= 20:
    #     pin_rojo.value(1)
    #     pin_verde.value(0)
    # elif peso >= 21:
    #     pin_verde.value(1)
    #     pin_rojo.value(0)