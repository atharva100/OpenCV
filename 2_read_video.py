import cv2 as cv

cap = cv.VideoCapture("resources/dog.mp4")

while True:
    success,img = cap.read()
    cv.imshow("dog_video",img)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break



