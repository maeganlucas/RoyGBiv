from colour import Color

import PIL
from PIL import ImageGrab
    # https://stackoverflow.com/questions/42636933/get-rgb-value-from-screen-pixels-with-python

import pyscreeze
    # https://stackoverflow.com/questions/42636933/get-rgb-value-from-screen-pixels-with-python

screen = pyscreeze.screenshot()

x = int(input("Please enter the x coordinate of the pixel: "))
y = int(input("Please enter the y coordinate of the pixel: "))

rgb = PIL.ImageGrab.grab().load()[x, y]

print(rgb)

if rgb == (255, 0, 0):
    print("\nRed")
elif rgb == (0, 255, 0):
    print("\nGreen")
elif rgb == (0, 0, 255):
    print("\nBlue")
