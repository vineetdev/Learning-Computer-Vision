# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:45:02 2021
@author: Vineet.Srivastava
Code which will demonstrate drawing circles
Usage: python drawingCircles.py
"""
import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")
(centerX, centerY) = (canvas.shape[1]//2, canvas.shape[0]//2)

white = (0, 255, 0)

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)
    
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype = "uint8")
for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 300, size = (2,))
    cv2.circle(canvas, tuple(pt), radius, color, -1)
    
cv2.imshow("RandomCircles", canvas)
cv2.waitKey(0)

    
