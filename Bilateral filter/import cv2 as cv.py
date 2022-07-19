import cv2 as cv
import numpy as np

img = cv.imread("11.jpeg", cv.IMREAD_GRAYSCALE)
bilateral = cv.bilateralFilter(img, 20, 80, 20)

cv.imwrite("11.jpeg",bilateral)