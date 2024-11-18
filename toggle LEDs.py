from machine import Pin
import time

# Set up input pins
redbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)
greenbutton = Pin(2, Pin.IN, Pin.PULL_DOWN)

# Set up output pins
redled = Pin(14, Pin.OUT)
greenled = Pin(25, Pin.OUT)

while True:

    time.sleep(0.2)
    
    if redbutton.value() == 1:
        redled.toggle()
        
    if greenbutton.value() == 1:
        greenled.toggle() 