import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3,640) #width; 3 is id number for width 
cap.set(4,480) #height; 4 is id number for height
cap.set(10,100) #brightness; 10 is id for brightness

while True: 
    success,img = cap.read()
    cv.imshow("Video",img)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break