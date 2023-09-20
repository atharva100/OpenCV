import cv2 as cv

cap = cv.imread("resources/lena.png")

cv.imshow("Output",cap)

cv.waitKey(0)
