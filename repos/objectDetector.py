import cv2 
import numpy as np
import os
import time
from windowcapture import WindowCapture
import win32api, win32gui, win32con


class Haar:
    def __init__(self, WindowName, Model):
    	self.wincap = WindowCapture('Aeldra')
    	self.Model = cv2.CascadeClassifier(Model)

    def setModel(self, Model):
    	self.Model = cv2.CascadeClassifier(Model)

    def setWindow(self, WindowName):
    	self.wincap = WindowCapture('Aeldra')

    def getScreenshot(self):
        self.screenshot = self.wincap.get_screenshot() 

    def detect(self):
    	self.rectangles = self.Model.detectMultiScale(self.screenshot, 1.5, 1)

   

har = Haar('Aeldra', 'Models/cascade.xml')
har.getScreenshot()
har.detect()
print(har.rectangles)
