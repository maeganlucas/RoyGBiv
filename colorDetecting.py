from colour import Color

import PIL
from PIL import ImageGrab
    # https://stackoverflow.com/questions/42636933/get-rgb-value-from-screen-pixels-with-python

import pyscreeze
    # https://stackoverflow.com/questions/42636933/get-rgb-value-from-screen-pixels-with-python

screen = pyscreeze.screenshot()

#Takes x-coordinate of desired pixel
x = int(input("Please enter the x coordinate of the pixel: "))
#Takes y-coordinate of desired pixel
y = int(input("Please enter the y coordinate of the pixel: "))

#Determines the RGB values of the pixel
rgb = PIL.ImageGrab.grab().load()[x, y]

#Prints the RGB value
print(rgb)

#Determines if the RGB value is pure red, blue, or green
if rgb == (255, 0, 0):
    print("\nRed")
elif rgb == (0, 255, 0):
    print("\nGreen")
elif rgb == (0, 0, 255):
    print("\nBlue")
