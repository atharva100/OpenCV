import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv.putText(img,"OpenCV",(300,200),cv.FONT_HERSHEY_COMPLEX,1,(150,150,0),1)

cv.imshow("img_text",img)
cv.waitKey(0) 