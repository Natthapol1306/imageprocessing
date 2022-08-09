import numpy as np
import cv2 as cv

img = cv.imread("pio.jpeg",cv.IMREAD_GRAYSCALE)

img = img.astype(np.float32);

imgF = np.fft.fft2(img)

imgF = np.fft.fftshift(imgF)

imgReal = np.real(imgF)
imglma = np.imag(imgF)
imgMag = np.sqrt(imgReal**2 + imglma**2)
imgPhs = np.arctan2(imglma, imgReal)

imgReallnv = imgMag*np.cos(imgPhs)
imglmalnv = imgMag*np.sin(imgPhs)

imgFlnv = imgReallnv + imglmalnv*1j

imgFlnv = np.fft.ifftshift(imgFlnv)
imglnv = np.fft.ifft2(imgFlnv)

imglnv = np.real(imglnv)
imglnv.astype(np.uint8)

cv.imwrite('input.png',img)
cv.imwrite('output.png',imglnv)

imgMag = np.log(1 + imgMag)
imgMag = cv.normalize(imgMag, None, 0, 255, cv.NORM_MINMAX, cv.CV_8U)

cv.imwrite("Mag.png",imgMag)

cv.imshow("Mag.png",imgMag)

cv.waitKey(0)

cv.destroyAllWindows()







