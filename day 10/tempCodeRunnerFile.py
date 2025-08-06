import cv2
import numpy as np 

cap=cv2.VideoCapture('vtest.avi')
while cap.isOpened():
    ret,frame=cap.read()
    cv2.imshow('inter',frame)
    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()
