import cv2
import numpy
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import PIL
from PIL import Image
from PIL import ImageGrab
import sys

# color correction citation from:
# https://www.irjet.net/archives/V7/i5/IRJET-V7I5687.pdf
# https://link.springer.com/content/pdf/10.1007/s41095-020-0172-x.pdf
# https://ixora.io/projects/colorblindness/daltonization/

def colorCorrectionDP(protanopia, deutranopia):
    return numpy.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],  [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

def daltonizationT():
    return

# Connect these values to the slider
deutranopia = 0.0  # unable to perceive red light
protanopia = 1.0 # unable to perceive green light
tritanopia = 0

#imgCorrected = numpy.array(Image.open("example.jpg")) / 255
imgCorrected = numpy.array(PIL.ImageGrab.grab()) / 255
transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
img_corrected = numpy.uint8(numpy.dot(imgCorrected, transform) * 255)
# Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.


cv2.imwrite("colorchange.jpg", img_corrected)


