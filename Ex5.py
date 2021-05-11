import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

pixels[16] = (127,3,252)
