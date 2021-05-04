import board
import neopixel

npix = 20

pixels = neopixel.NeoPixel(board.D18, npix)

pixels[-1] = (0,50,0)
