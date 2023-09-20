import cv2 as cv
import numpy as np

img = cv.imread("resources/lambo.png")
print(img.shape)

imgResize = cv.resize(img,(300,200)) #(width,height)
print(imgResize.shape)

cv.imshow("lambo_img",img)
cv.imshow("lambo_resized",imgResize)

cv.waitKey(0)


