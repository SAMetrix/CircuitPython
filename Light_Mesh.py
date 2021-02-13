import board
import neopixel
import time

pixel = neopixel.NeoPixel(board.GP15, 24, brightness=0.1)

Off = (0,0,0)
red = (255,0,0)
blue = (0,0,255)

def mesh():
    for i in range(24):
        if (i % 2 != 0):
            pixel[i] = red
            time.sleep(0.1)
        elif (i % 2 == 0 or i == 0):
            if (i == 0):
                time.sleep(0.1)
                pixel[0] = blue
            else:
                pixel[24 - i] = blue
                time.sleep(0.1)
                
                
def mesh_off():
    for i in range(24):
        if (i % 2 != 0):
            pixel[i] = Off
            time.sleep(0.1)
        elif (i % 2 == 0 or i == 0):
            if (i == 0):
                time.sleep(0.1)
                pixel[0] = Off
            else:
                pixel[24 - i] = Off
                time.sleep(0.1)
           
            
            

while True:
    mesh()
    mesh_off()
#pixel[0] = blue
            
            