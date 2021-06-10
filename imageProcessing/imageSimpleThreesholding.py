# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 17:43:40 2021

@author: Vineet.Srivastava
Demonstrates usage of simple thresholding
Usage: python imageSimpleThreesholding.py -i images/coins.png
"""
import numpy as np
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

''' Convert image to grayscale '''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

''' Smooth it out '''
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("image", blurred)

''' Apply thresholding '''
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary Gaussian", thresh)

''' Apply the inverse '''
(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

''' Use the inverse as mask to get to focus only on coins '''
cv2.imshow("Coins", cv2.bitwise_and(gray, gray, mask = threshInv))

cv2.waitKey(0)