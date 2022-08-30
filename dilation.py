import cv2 as cv
import numpy as np

img = cv.imread('Pra.jpeg',0)
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))

erosion = cv.erode(img,kernel,iterations=10)

dilation = cv.dilate(img,kernel,iterations=10)

cv.imwrite('output_eros.png', erosion)
cv.imwrite('output_dilation.png', dilation)