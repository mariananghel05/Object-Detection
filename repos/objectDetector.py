import cv2 
import numpy as np
import os
import time
from windowcapture import WindowCapture
import win32api, win32gui, win32con
from Draw import Draw


wincap = WindowCapture('Aeldra')
Model = cv2.CascadeClassifier("Models/cascade.xml")
loop_time = time.time()

while(True):
    screen = wincap.get_screenshot()
    detection = Model.detectMultiScale(screen, 1.15, 2)

    draw = Draw()
    draw.DrawRectangle(screen, detection)
    draw.DrawPoint(screen, detection, 1)
    draw.putText(screen, detection, "Devil Metin")

    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()
    
    cv2.imshow('Metin2', screen)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
