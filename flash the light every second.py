from machine import Pin
from time import sleep

LED = Pin(25, Pin.OUT)
LED.value(1)
i = 0

while i < 30:
    i += 1
    print(LED.value())
    if LED.value() == 1:
        newLEDState = 0
    else:
        newLEDState = 1
    print(newLEDState)
    LED.value(newLEDState)
    sleep(1)


