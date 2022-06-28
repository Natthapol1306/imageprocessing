import numpy as np
import cv2 as cv

img = cv.imread("USA.jpeg",cv.IMREAD_GRAYSCALE)

output = cv.medianBlur(img,5)

cv.imwrite('Median[1]input.png',img)
cv.imwrite('Median[2]output.png',output)
