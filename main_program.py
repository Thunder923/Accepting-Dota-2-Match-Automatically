import numpy as np
import cv2
import time
from py2 import PressKey,ReleaseKey,W,S,A,D,C,Enter
import keyboard
import sys
from PIL import ImageGrab
th1 = cv2.imread('matchimage1.png')
i = 0
global start_timer
from tkinter import Tk
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(width,height)
start_timer = time.time()
while True:
    i = i + 1
    if keyboard.is_pressed('esc'):
        
        elapsed = time.time() - start_timer
        print((elapsed/60)/60,"Hour")
        print(elapsed/60,"Min")
        print(elapsed,"Sec")
        break

    #time.sleep(0)
    Print_Screen = ImageGrab.grab()
    Print_Numpy = np.array(Print_Screen)
    x,y,w,h = bbox = (600, 460, 650, 150)
    x1,y1,w1,h1 = 0,0,0,0
    x1 = (x*1920)/100
    x1 =  (x1*100)/width
    w1 = (w*1920)/100
    w1 =  (w1*100)/width


    y1 = (y*1080)/100
    y1 = (y1*100)/height
    h1 = (h*1080)/100
    h1 = (h1*100)/height
    croped = Print_Numpy[int(y1):int(y1)+int(h1), int(x1):int(x1)+int(w1)]
    th2 = cv2.cvtColor(croped, cv2.COLOR_BGR2RGB)
    iar = np.array(th1)
    iar2 = np.array(th2)
    matched_arrays = 0
    x = 0      
    while (x < h1):
        y = 0
        while (y < w1 ):   
            if (iar[x][y] == iar2[x][y]).all():
                matched_arrays = matched_arrays + 1
            y  = y + 1
        x = x + 1
        if x == iar.size:
            break
    percent = (matched_arrays / (h1*w1)) * 100
    if percent > 90:
        PressKey(Enter)
        print(int(percent),"%")
        time.sleep(3)
print("Number of time loop ran: "+i)


