# -*- coding: utf-8 -*-
"""
Created on Mon May 31 19:28:21 2021
@author: Vineet.Srivastava
Code which will demonstrate drawing lines and rectangles
Usage: python DrawingLines.py
"""
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")
cv2.imshow("Drawing Canvas", canvas)

green = (0, 255, 0)
cv2.line(canvas, (0,0), (300, 300), green)
cv2.imshow("Drawing Green Line", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
cv2.line(canvas, (0,300), (300, 0), red, 3)
cv2.imshow("Drawing Red Line", canvas)
cv2.waitKey(0)

cv2.rectangle(canvas, (10, 10), (100, 100), green, 2)
cv2.imshow("Drawing Rectangle", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
# thickness -1 for filling in the rectangle 
# thickness positive value for boundary value
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Drawing Another Rectangle", canvas)
cv2.waitKey(0)


