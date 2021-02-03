import board
import neopixel
import time

pixel = neopixel.NeoPixel(board.GP15, 24, brightness=0.1)

Off = (0,0,0)

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

def left_right_loop():
    for i in range(1):
        for j in range(12):
            pixel_index = (j * 255 // 12) + i
            pixel[j] = wheel(pixel_index & 255)
            pixel[23-j] = wheel(pixel_index & 255)
            time.sleep(0.2)
            

def left_right_opposite_loop():
    for i in range(1):
        for j in range(11, -1, -1):
            pixel_index = (j * 255 // 12) + i
            pixel[j] = wheel(pixel_index & 255)
            pixel[12+j] = wheel(pixel_index & 255)
            time.sleep(0.2)

            
            
            
def turn_off_left_right():
    for i in range(12):
        pixel[i] = Off
        pixel[23-i] = Off
        time.sleep(0.2)
        
        
def turn_off_left_right_opposite():
    for i in range(11, -1, -1):
        pixel[i] = Off
        pixel[12+i] = Off
        time.sleep(0.2)
    
        
        
while True:       
    left_right_loop()
    turn_off_left_right()
    left_right_opposite_loop()
    turn_off_left_right_opposite()
    
    

