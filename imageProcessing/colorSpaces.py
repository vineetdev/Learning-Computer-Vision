# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:04:10 2021

@author: Vineet.Srivastava
Demonstrates as to how to change color spaces using OpenCV
Usage: python colorSpaces.py -i images/beach.png
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY", gray)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
cv2.imshow("l*a*b*", lab)

cv2.waitKey(0)
