import numpy as np
import cv2 as cv

#Read the image
img = cv.imread("USA.jpeg", cv.IMREAD_GRATSCALE)

# Apply Filter to lmage
output = cv.medianBlur(img,5)

cv.imwrite('Median[1]input.png', img)
cv.imwrite('Median[2]output.png', output)
