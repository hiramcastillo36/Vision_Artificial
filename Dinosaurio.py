import numpy as np
from PIL import ImageGrab
import cv2
import time
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")

Hmin=26
Hmax=255
Smin=123
Smax=255
Vmin=44
Vmax=255

contador=0
last_time = time.time()
while(True):
    minimo=np.array([Hmin,Smin,Vmin])
    maximo=np.array([Hmax,Smax,Vmax])
    # 800x600 windowed mode
    printscreen =  np.array(ImageGrab.grab(bbox=(0,40,410,585)))
    gray= cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('gray',gray)
    blur= cv2.GaussianBlur(printscreen,(7,7),0)
    #cv2.imshow('blur',blur)
    hsv= cv2.cvtColor(printscreen, cv2.COLOR_BGR2HSV)
    #cv2.imshow('hsv',hsv)
    union= cv2.inRange(hsv, minimo, maximo)
    f1= cv2.erode(union, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
    f2= cv2.erode(f1, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
    object= cv2.moments(f2)
    last_time = time.time()
    #cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))

    if object['m00'] > 10:
        cx= int(object['m10']/object['m00'])
        cy= int(object['m01']/object['m00'])
        cv2.circle(printscreen, (cx,cy), 15, (0,255,0), 2)
        if cx > 150 and cx < 380 and cy> 280:
            shell.SendKeys("{UP}")
            contador=contador+1

    cv2.imshow('xd',printscreen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()
