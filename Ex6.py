import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 20)

#red
for i in range (6):
    pixles[i] = (10,0,0)

#blue
for i in range (5,20):
    pixles[i] = (0,0,252)
