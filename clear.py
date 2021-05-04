import board
import neopixel

npix = 20

pixels = neopixel.NeoPixel(board.D18, npix)

for i in range(npix):
	pixels[i] = (0,0,0)

