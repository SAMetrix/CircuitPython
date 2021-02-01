import board
import neopixel
import time
import random

pixel = neopixel.NeoPixel(board.GP15, 24, pixel_order = neopixel.RGB, brightness=0.1)
Red = (0,255,0)
Blue = (0,0,255)
Off = (0,0,0)

def evenAlternate():
    for i in range(24):
        if (i%2 == 0):
            pixel[i] = Red
        else:
            if (i%2 != 0):
                time.sleep(0.2)
                pixel[i] = Off
        #if (i < 24):
           # pixel[i+1] = Off
    #time.sleep(0.2)
           
def oddAlternate():
    for j in range(24):
        if (j%2 != 0 and j!=0):
            pixel[j] = Blue
        else:
            if (j%2 == 0):
                time.sleep(0.2)
                pixel[j] = Off
           # pixel[23] = Off
           # pixel[j-1] = Off
        
        
        
while True:        
    evenAlternate()
    time.sleep(0.2)
    oddAlternate()
    time.sleep(0.2)
#pixel[23] = Off

