import cv2 as cv
import numpy as np

img = cv.imread("resources/lena.png")
kernel = np.ones((5,5),np.uint8)

#gray image
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#blur image
imgBlur = cv.GaussianBlur(imgGray,(7,7),0) #kernal-size=(7,7) and sigmax=0
#edge detecter
imgCanny = cv.Canny(img,150,200)
#to increase the thickness of edge
imgDialation = cv.dilate(imgCanny,kernel,iterations=1)
#to decrease the thickness of edge
imgEroded = cv.erode(imgDialation,kernel,iterations=1)

cv.imshow("Blur image",imgBlur)
cv.imshow("Gray image",imgGray)
cv.imshow("Canny image",imgCanny)
cv.imshow("Dialation image",imgDialation)
cv.imshow("Eroded image",imgEroded)

cv.waitKey(0)