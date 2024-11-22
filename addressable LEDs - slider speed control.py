# Imports
import time
from machine import Pin, ADC
from neopixel import NeoPixel
import random

# Set up the slider on ADC pin 28
potentiometer = ADC(Pin(28))

# Define the LED pin number (2) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

# Create a flash speed variable
flash = 0

while True:
    
    # Read the potentiometer value
    flash = potentiometer.read_u16() / 65000
    
    # Generate random GRB values
    g1 = random.randint(0,255)
    r1 = random.randint(0,255)
    b1 = random.randint(0,255)
    g2 = random.randint(0,255)
    r2 = random.randint(0,255)
    b2 = random.randint(0,255)
     
    # Light the LED with the random GRB values
    GRBled1.fill((g1,r1,b1))
    GRBled1.write()
    GRBled2.fill((g2,r2,b2))
    GRBled2.write()
    
    # Delay based on slider position
    time.sleep(flash)
