import cv2 as cv
import numpy as np

""" note :
    zeroes = black 
    in OpenCV the color notation instead of RGB is BGR"""


img = np.zeros((512,512,3),np.uint8)

#whole image turns blue
# img[:] = 250,0,0  

#turns the following area under the dimensions blue
# img[200:300,100:300] = 250,0,0 

#drawing green line - (image_var,starting_point,ending_point,color,thickness)
#cv.line(img,(0,0),(300,300),(0,255,0),3)

#drawing line till the end of the image
#cv.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

# line without filled rectangle
# cv.rectangle(img,(0,0),(250,350),(0,0,255),2)

# filled rectangle
# cv.rectangle(img,(0,0),(250,350),(0,0,255),cv.FILLED)

# circle
cv.circle(img,(400,50),30,(255,255,0),cv.FILLED) 

cv.imshow("image",img)

cv.waitKey(0)