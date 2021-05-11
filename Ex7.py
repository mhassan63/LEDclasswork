import board
import neopixel
import time

npix = 21
pixels = neopixel.NeoPixel(board.D18, npix)

for i in range (npix):
    pixels [i] = (98,252,3)
    time.sleep(.25)
