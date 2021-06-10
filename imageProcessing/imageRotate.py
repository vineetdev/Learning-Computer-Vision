# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:47:51 2021

@author: Vineet.Srivastava
Code to demonstrate image rotation
Usage: python imageRotate.py -i images/trex.png
"""
import numpy as np
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

(h, w) = image.shape[:2]
center = (w // 2, h // 2)

# Get the Rotation Matrix for rotation by 45 degrees UP 
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 degrees Up", rotated)

# Get the Rotation Matrix for rotation by 90 degrees UP 
M = cv2.getRotationMatrix2D(center, -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 90 degrees Up", rotated)

''' rotate image by 180 degrees '''
rotated = imutils.rotate(image, -180)
cv2.imshow("Rotated 180 degrees", rotated)

cv2.waitKey(0)