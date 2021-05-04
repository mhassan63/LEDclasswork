import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[2] = (0,250,0)


