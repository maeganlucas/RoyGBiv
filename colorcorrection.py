import cv2
import numpy
import PIL
from PIL import ImageGrab
from colorblind import colorblind

# color correction citation from:
# https://www.irjet.net/archives/V7/i5/IRJET-V7I5687.pdf
# https://link.springer.com/content/pdf/10.1007/s41095-020-0172-x.pdf
# https://ixora.io/projects/colorblindness/daltonization/

def colorCorrectionDP(protanopia, deutranopia):
    return numpy.array([[1 - deutranopia / 2, deutranopia / 2, 0], [protanopia / 2, 1 - protanopia / 2, 0],  [protanopia / 4, deutranopia / 4, 1 - (protanopia + deutranopia) / 4]]).T

# https://ixora.io/projects/colorblindness/color-blindness-simulation-research/used for matrix
def Tritanopia(img):
    colorblind_img = colorblind.simulate_colorblindness(img, colorblind_type='t')
    defection = img - colorblind_img
    correction = numpy.array([[0, 0, 0], [0.7, 1, 0], [0.7, 0, 1]])
    Daltonization = numpy.tensordot(defection, correction, axes=([2], [1]))
    return img + Daltonization

# Connect these values to the slider
deutranopia = 0.0  # unable to perceive red light
protanopia = 1.0 # unable to perceive green light
tritanopia = 0 # NO CURRENT OPTION FOR A TRITANOPIA SLIDER / MUST BE MUTUALLY EXCLUSIVE FROM DUETRANOPIA AND PROTANOPIA

#imgCorrected = numpy.array(Image.open("example.jpg")) / 255
imgCorrected = numpy.array(PIL.ImageGrab.grab()) / 255
transform = colorCorrectionDP(protanopia=protanopia, deutranopia=deutranopia)
img_correctedPD = numpy.uint8(numpy.dot(imgCorrected, transform) * 255)
# Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
imgDaltonized = Tritanopia(PIL.ImageGrab.grab())
cv2.imwrite("colorchangePD.jpg", img_correctedPD)
cv2.imwrite("colorchangeT.jpg", imgDaltonized)


