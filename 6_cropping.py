import cv2 as cv
import numpy as np

img = cv.imread("resources/lambo.png")
print(img.shape)

#[height,width]
imgCropped = img[0:200,200:500]

cv.imshow("image",img)
cv.imshow("image_cropped",imgCropped)

cv.waitKey(0)