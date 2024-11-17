from machine import Pin
from time import sleep

greenLED = Pin(25, Pin.OUT) ## internal to the Raspberry Pi Pico H
redLED = Pin(14, Pin.OUT) ## added to GP14 (number 19 on the board itself)
greenLED.value(0)

j = 0
k = 0
l = 0
myFuckingSoulNeedsSaving = True

sleep(1)

while myFuckingSoulNeedsSaving:
    i = 0
    j = 0
    k = 0
    while i < 6:
        i += 1
        if greenLED.value() == 1:
            newLEDState = 0
        else:
            newLEDState = 1
        greenLED.value(newLEDState)
        redLED.value(newLEDState)
        sleep(0.2)
    j = 0
    newLEDState = 0
    sleep(0.5)
    while j < 6:
        j += 1
        if greenLED.value() == 1:
            newLEDState = 0
        else:
            newLEDState = 1
        greenLED.value(newLEDState)
        redLED.value(newLEDState)
        sleep(1)
    k = 0
    newLEDState = 0
    while k < 6:
        k += 1
        if greenLED.value() == 1:
            newLEDState = 0
        else:
            newLEDState = 1
        greenLED.value(newLEDState)
        redLED.value(newLEDState)
        sleep(0.2)
    sleep(3)
    greenLED.value(0)
    redLED.value(newLEDState)