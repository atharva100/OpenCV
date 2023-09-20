import cv2 as cv
import numpy as np

# to get its bird eye view we use warp prespective
img = cv.imread("resources/cards.jpg")

# getting the points of kings of spades in the cards
# you can get the values from paint 
width,height = 250,350

pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(img,matrix,(width,height))

cv.imshow("image",img)
cv.imshow("image_Output",imgOutput)

cv.waitKey(0)