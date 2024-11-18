from machine import Pin
import time

# Set up the LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

segments = [seg1, seg2, seg3, seg4, seg5]

while True:
    for led in segments:
        led.value(1)
        time.sleep(0.08)
        led.value(0)
        
    for led in reversed (segments):
        led.value(1)
        time.sleep(0.08)
        led.value(0)
