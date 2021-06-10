# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:17:35 2021

@author: Vineet.Srivastava
Demonstrates adaptive thresholding in image processing and with final note
on how to choose among the different types of adaptive thresholding.
Usage: python imageAdaptiveThresholding.py -i images/coins.png
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["i"])
cv2.imshow("Original Image", image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred Image", blurred)

''' Apply adaptive thresholding with mean weighted method'''
''' neighborhood size is kept as 11, 
    parameter C is 4 which will be substracted from the mean '''
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", thresh)

''' Apply adaptive thresholding with Gaussian weighted method '''
''' neighborhood size is kept as 15, 
    parameter C is 3 which will be substracted from the mean '''
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)

''' Here the results of above two methods is more or less the same '''
''' Which method to choose among them will require a few experiments at 
    your end with the values of neighborhood sizes and parameter C. 
    By experimenting with these values, you should be able to dramatically 
    change the result of thresholding '''
    
cv2.waitKey(0)
