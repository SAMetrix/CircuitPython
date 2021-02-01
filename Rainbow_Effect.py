import board
import neopixel
import time

pixel = neopixel.NeoPixel(board.GP15, 24, brightness=0.1, auto_write=False)

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



def rainbow():
    for i in range(255):
        for j in range(24):
            pixel_index = (j * 255 // 24) + i
            pixel[j] = wheel(pixel_index & 255)
        pixel.show()
            

while True:
    rainbow()