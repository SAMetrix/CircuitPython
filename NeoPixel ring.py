import board
import neopixel
import time
import random

pixel = neopixel.NeoPixel(board.GP15, 24, pixel_order = neopixel.RGB, brightness=0.3)

#color = (0,22,0)
#testing
#for i in range(23):
 #   pixel[i] = color
  #  #time.sleep(0.1)
   # pixel[i] = (0,0,0)
    #time.sleep(0.2)
    #pixel[i+1] = color
    
# for j in range(23,0,-1):
#     #pixel[j] = (0,0,0)
#     time.sleep(0.2)
#     if (j != 23):
#         pixel[j] = color
#     print(j)
#     time.sleep(0.2)
    
#     for i in range(23):
#         print(i)
#         pixel[i] = color
#         #time.sleep(0.1)
#         pixel[i] = (0,0,0)    
#         time.sleep(0.2)
#         pixel[i+1] = color
#         #print(pixel[i])

while True:
    for j in range(23,-1,-1):
    
        for i in range(24):
            color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            if(i > j):
                continue
            else:
                if(i == 0 or i > j):
                    pass
                else:
                    pixel[i-1] = (0,0,0)
                print(i,j)
                pixel[i] = color
                if (j != 23):
    #                 if (j == 1):
    #                     pixel[j] = color
                    pixel[j+1] = color
                time.sleep(0.1)
    #pixel[j] = color
    

    

#pixel[0] = (255,0,0)
#pixel[1] = (255,255,0)
#pixel[2] = (255,255,255)
#pixel[2] = (0,0,0)
#pixel[1] = (0,0,0)
#pixel[0] = (0,0,0)
            
            
            