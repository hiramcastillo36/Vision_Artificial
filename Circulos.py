import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('Hue Minimo','image',0,255,nothing)
cv2.createTrackbar('Hue Maximo','image',0,255,nothing)
cv2.createTrackbar('Saturation Minimo','image',0,255,nothing)
cv2.createTrackbar('Saturation Maximo','image',0,255,nothing)
cv2.createTrackbar('Value Minimo','image',0,255,nothing)
cv2.createTrackbar('Value Maximo','image',0,255,nothing)

while True:
    ret, frame = cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hMin=cv2.getTrackbarPos('Hue Minimo','image')
    hMax=cv2.getTrackbarPos('Hue Maximo','image')
    sMin=cv2.getTrackbarPos('Saturation Minimo','image')
    sMax=cv2.getTrackbarPos('Saturation Maximo','image')
    vMin=cv2.getTrackbarPos('Value Minimo','image')
    vMax=cv2.getTrackbarPos('Value Maximo','image')

    lower=np.array([hMin,sMin,vMin])
    upper=np.array([hMax,sMax,vMax])

    mask=cv2.inRange(hsv,lower,upper)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
