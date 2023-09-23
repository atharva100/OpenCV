import cv2 as cv
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColors = [[0,126,0,59,255,255],      #orange
            [96,82,0,139,255,255],    #purple
            [47,80,0,83,255,255]]     #green

myColorValues = [[51,153,255],
                 [255,0,255],
                 [0,255,0]]  #BGR

myPoints = []  #[x,y,colorId]

def findColor(img,myColors,myColorValues):
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(imgHSV,lower,upper)
        x,y = getContours(mask)
        cv.circle(imgResult,(x,y),10,myColorValues[count],cv.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
        # cv.imshow(str(color[0]),mask)
    return newPoints

def getContours(img):
    countours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in countours:
        area = cv.contourArea(cnt)
        if area>500: 
            # cv.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv.boundingRect(approx)
    return x+w//2,y

def DrawOnCanvas(myPoints,myColorValues):
    for point in myPoints: 
        cv.circle(imgResult,(point[0],point[1]),10,myColorValues[point[2]],cv.FILLED)


while True: 
    success,img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        DrawOnCanvas(myPoints,myColorValues)

    cv.imshow("Result",imgResult)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break