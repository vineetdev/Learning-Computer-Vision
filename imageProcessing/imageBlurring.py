# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 12:31:26 2021
@author: Vineet.Srivastava
Demonstrates Image Blurring
Usage: python imageBlurring.py -i images/trex.png
"""
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#cv2.imshow("Original Image", image)

''' Average blurring '''
blurred = np.hstack([
    image,
    cv2.blur(image, (3, 3)),
    cv2.blur(image, (5, 5)),
    cv2.blur(image, (7, 7))])
cv2.imshow("BLURRED", blurred)

''' Gaussian blurring '''
''' Third parameter is the Standard Deviation in the x-axis direction
    By 0 we are telling OpenCV to automatically compute based on kernel size '''
blurredgaussian = np.hstack([
    cv2.GaussianBlur(image, (3, 3), 0),
    cv2.GaussianBlur(image, (5, 5), 0),
    cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("GAUSSIAN BLURRED", blurredgaussian)

''' Median blurring '''
''' Used for removing salt and pepper noise '''
blurredmedian = np.hstack([
    cv2.medianBlur(image, 3),
    cv2.medianBlur(image, 5),
    cv2.medianBlur(image, 7)])
cv2.imshow("MEDIAN BLURRED", blurredmedian)
''' this removes motion blur '''

''' Bilateral blurring '''
''' this removes noise keeping the edges in picture intact '''
blurredbilateral = np.hstack([
    cv2.bilateralFilter(image, 5, 21, 21),
    cv2.bilateralFilter(image, 7, 31, 31),
    cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("BILATERAL BLURRED", blurredbilateral)

cv2.waitKey(0)