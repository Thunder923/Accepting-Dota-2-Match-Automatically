import numpy as np
import cv2
import time
from py2 import PressKey,ReleaseKey,W,S,A,D,C,Enter
import keyboard
from PIL import ImageGrab

newimg = cv2.imread('matchimage1.png')
th1 = cv2.Canny(newimg,threshold1 =200,threshold2 = 300)

#cv2.imshow('123',grayimg1)
while True:
    if keyboard.is_pressed('esc'):
        break
    time.sleep(0)
    Print_Screen = ImageGrab.grab()
   # Print_Numpy = np.array(Print_Screen.getdata(),dtype='uint8')\
    #.reshape((Print_Screen.size[1],Print_Screen.size[0],3))
    Print_Numpy = np.array(Print_Screen)
    x,y,w,h = bbox = (600, 460, 650, 150)
    croped = Print_Numpy[y:y+h, x:x+w]
    th2 = cv2.Canny(croped,threshold1 =200,threshold2 = 300)
    #cv2.imshow('abc',th2)
    iar = np.array(th1)
    iar2 = np.array(th2)

    if (iar == iar2).all():
        PressKey(Enter)
        print("Matched")
        time.sleep(3)
    else:
        print("Not mATched")



