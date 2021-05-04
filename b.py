import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[18] = (0,0,100)
