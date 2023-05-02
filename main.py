import machine
import time
from machine import SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from stepper import create

def drop_current(fruto,dic):
    if fruto == "Mani":
        return dic["Mani"][0], dic["Mani"][1]
    elif fruto == "Nueces":
        return dic["Nueces"][0], dic["Nueces"][1]
    elif fruto == "Almendras":
        return dic["Almendras"][0], dic["Almendras"][1]

def change_delay(fruto,dic):
    if fruto == "Mani":
        dic["Mani"][1] = 4
    #elif fruto == "Nueces":
    #    return dic["Nueces"][0], dic["Nueces"][1]
    #elif fruto == "Almendras":
    #    return dic["Almendras"][0], dic["Almendras"][1]

led_verde = machine.Pin(27, machine.Pin.OUT)
led_rojo = machine.Pin(23,machine.Pin.OUT)

boton = machine.Pin(25, machine.Pin.IN)
boton_drop = machine.Pin(32,machine.Pin.IN)

motor1 = machine.Pin(15,machine.Pin.OUT)
motor2 = machine.Pin(2,machine.Pin.OUT)
motor3 = machine.Pin(4,machine.Pin.OUT)
motor4 = machine.Pin(5,machine.Pin.OUT)

sensor = machine.Pin(34,machine.Pin.IN)

led_verde.value(0)
led_rojo.value(0)

boton.value(0)
frutos_secos = ["Mani", "Nueces", "Almendras"]
caida = {"Mani":[130,1],"Nueces":[360,2],"Almendras":[360,4]} #diccionario con [0] angulo y [1] delay
fruto = 0

#LCD
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=machine.Pin(21), sda=machine.Pin(22), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
    val = boton.value()
    if val: # boton para cambiar el fruto seco
        lcd.clear()
        current = frutos_secos[fruto]
        lcd.putstr(frutos_secos[fruto])
        # print(current)
        time.sleep(0.1)
        fruto += 1
        if fruto == 3:
            fruto = 0
        boton.value(0)
    time.sleep(0.1)

    if boton_drop.value():
        try:
            angle,delay = drop_current(current,caida) # si apreto el boton
#             print("antesss", caida["Mani"][1])
            s1 = create(motor1,motor2,motor3,motor4,delay) #creo un motor con el delay que corresponda al fruto seco que está seleccionado.
            s1.reset()
            s1.step(1,1)
            s1.angle(angle) #ver si da vuelta completa 
#             time.sleep(0.009)
#             s1.step(1,-1)
#             s1.angle(angle,-1)
            boton_drop.value(0)
        except NameError:
            pass    
    
    if sensor.value(): #no apunta a nada
        led_rojo.value(1)
        led_verde.value(0)
        
#         try:
#             change_delay(current,caida)
#             #print(" despues", caida["Mani"][1])
#         except NameError:
#             pass
        
    else: # apunta a algo
        led_verde.value(1)
        led_rojo.value(0)
       # print("antesss", caida["Mani"][1])

    time.sleep(0.1)