import cv2 as cv
import random

img = cv.imread('6310301023_a.png', cv.IMREAD_GRAYSCALE)

density_salt = 0.1
density_pepper = 0.1

number_of_white_pixel = int(density_salt*(img.shape[0]*img.shape[1]))
output = cv.medianBlur(img,5)

for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0]-1)
    x_coord = random.randint(0, img.shape[1]-1)
    img[y_coord][x_coord] = 255

number_of_black_pixel  = int(density_pepper*(img.shape[0] * img.shape[1]))

for i in range(number_of_black_pixel):
    y_coord = random.randint(0, img.shape[0]-1)
    x_coord = random.randint(0, img.shape[1]-1)
    img[y_coord][x_coord] = 0

cv.imwrite('6310301023_b.png', img)
cv.imwrite('6310301023_c.png',output)