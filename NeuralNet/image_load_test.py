import cv2
import numpy

im = cv2.imread("test.png")
im = numpy.divide(im, 255)
im = im.flatten()
print(size(im))