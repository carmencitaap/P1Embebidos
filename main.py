import machine
import time
from machine import SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

pin_verde = machine.Pin(27, machine.Pin.OUT)
boton = machine.Pin(25, machine.Pin.IN)
pin_verde.value(0)

boton.value(0)
frutos_secos = ["Mani", "Nueces", "Almendras"]
fruto = 0

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=machine.Pin(21), sda=machine.Pin(22), freq=10000)
lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

while True:
    val = boton.value()

    if val:
        print(fruto)
        lcd.clear()
        print(frutos_secos[fruto])
        lcd.putstr(frutos_secos[fruto])
        pin_verde.value(1)
        time.sleep(0.1)
        fruto += 1
        if fruto == 3:
            fruto = 0
        boton.value(0)
    time.sleep(0.1)