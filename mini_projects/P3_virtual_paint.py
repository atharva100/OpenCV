import cv2 as cv
import numpy as np


frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)


myColors = [[50,109,52,255,0,255],     #green
            [0,11,94,255,0,255],    #orange
            [39,133,40,255,0,255]]      #purple



def findColor(img,myColors):
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV,lower,upper)
        getContours(mask)
        #cv.imshow(str(color[0]),mask)

def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500:
            cv.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv.boundingRect(approx)



while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors)
    cv.imshow("Result", imgResult)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

