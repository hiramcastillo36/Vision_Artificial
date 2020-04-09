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
minimo=np.array([Hmin,Smin,Vmin])
maximo=np.array([Hmax,Smax,Vmax])

while(True):
    # 800x600 windowed mode
    printscreen =  np.array(ImageGrab.grab(bbox=(1,40,380,650)))
    hsv= cv2.cvtColor(printscreen, cv2.COLOR_BGR2HSV)
    union= cv2.inRange(hsv, minimo, maximo)
    f1= cv2.erode(union, cv2.getStructuringElement(cv2.MORPH_RECT,(3,3)), iterations=1)
    f2= cv2.erode(f1, cv2.getStructuringElement(cv2.MORPH_RECT,(5,5)), iterations=1)
    object= cv2.moments(f2)
    if object['m00'] > 5:
        cx= int(object['m10']/object['m00'])
        cy= int(object['m01']/object['m00'])
        cv2.circle(printscreen, (cx,cy), 20, (0,255,0), 1)
        if cx > 230 and cx < 360 and cy>280:
            shell.SendKeys("{UP}")


    #cv2.imshow('xd',printscreen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
cv2.destroyAllWindows()
