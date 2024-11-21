import time
from machine import Pin
from neopixel import NeoPixel
import _thread

# Define the LED pin number (2) and number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

#bar LEDs
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Define some GRB colour variables
white = 240,140,255 #White-ish!
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238, 223, 105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215, 100, 0

# Define our colour list
colours = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]
segments = [seg1, seg2, seg3, seg4, seg5]

def loop_a():
    while True:  
        for colour in colours:
            
            GRBled1.fill((colour))
            
            GRBled1.write()
            
            time.sleep(0.5)
            
def loop_b():
    while True:      
        for colour in reversed (colours):
            
            GRBled2.fill((colour))
            
            GRBled2.write()
            
            time.sleep(0.2)
            
def loop_c():
    #while True:
        for led in segments:
            led.value(1)
            time.sleep(0.08)
            led.value(0)
            
        for led in reversed (segments):
            led.value(1)
            time.sleep(0.08)
            led.value(0)
            
second_thread = _thread.start_new_thread(loop_b,())

#third_thread = _thread.start_new_thread(loop_c, ())

loop_a()
            
# TaskQueue = [ loop_a(), loop_b(), loop_c()]
# 
# while True:
#     for task in TaskQueue:
#         next(task)
