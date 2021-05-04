import board
import neopixel
import time 

pixels = neopixel.NeoPixel (board.D18,20)

for i in range(19,0,-1):
	pixels[i] = (252,82,3)
	time.sleep(.3)
