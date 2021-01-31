import time
import board
from analogio import AnalogIn
import neopixel
import random

analog_in = AnalogIn(board.GP26_A0)
pixel = neopixel.NeoPixel(board.GP15, 24, pixel_order = neopixel.RGB, brightness=0.3)

Blue = (0,0,255)
Black = (0,0,0)


def map_range(x, in_min, in_max, out_min, out_max):
    """
    Maps a number from one range to another.
    Note: This implementation handles values < in_min differently than arduino's map function does.

    :return: Returns value mapped to new range
    :rtype: float
    """
    in_range = in_max - in_min
    in_delta = x - in_min
    if in_range != 0:
        mapped = in_delta / in_range
    elif in_delta != 0:
        mapped = in_delta
    else:
        mapped = 0.5
    mapped *= out_max - out_min
    mapped += out_min
    if out_min <= out_max:
        return max(min(mapped, out_max), out_min)
    return min(max(mapped, out_max), out_min)

def get_Voltage(pin):
    mapled= map_range(pin, 1900, 2100, 0, 23)
    return int(mapled)

def LedLevel(start,stop, color):
    #print(level)
    d=1
    if (start > stop):
        d = -1
    for i in range(start,stop,d):
        if (color == (0,0,0)):
            pixel[i] = color
        else:
            pixel[i] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        time.sleep(0.025)
    


while True:
   # c = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    currentLevel = get_Voltage(analog_in.value)
    LedLevel(0,currentLevel, Blue)
    #time.sleep(0.1)

    newLevel = get_Voltage(analog_in.value)
    LedLevel(currentLevel, 0, Black)
    #print(currentLevel, newLevel)
    #time.sleep(0.1)