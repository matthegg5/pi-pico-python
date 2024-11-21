import time
from machine import Pin
from neopixel import NeoPixel

# Define the LED pin number (2) and number of LEDs (1)
GRBled = NeoPixel(Pin(2), 1)

while True:
    
# Fill the LED with blue (GRB)
    GRBled.fill((0,0,255))
    GRBled.write()
    time.sleep(0.5)
    GRBled.fill((255,0,0))
    GRBled.write()
    time.sleep(0.5)
    GRBled.fill((0,255,0))
    GRBled.write()
    time.sleep(0.5)
    GRBled.fill((181,6,255))
    GRBled.write()
    sleep(0.5)
        
# Write the data to the LED