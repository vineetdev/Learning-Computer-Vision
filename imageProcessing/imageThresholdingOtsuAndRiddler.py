# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 18:37:11 2021
@author: Vineet.Srivastava
Demonstrates Otsu and Riddler-Calvard method of calculation of Thresholding
Usage: python imageThresholdingOtsuAndRiddler.py -i images/coins.png
"""
from __future__ import print_function
import numpy as np
import argparse
import mahotas
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred Image", blurred)

''' Otsu's thresholding method '''
''' Step1. Lets get the optimal value of T '''
T = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(T))

''' Step2. Lets apply the thresholding value '''
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
''' Step3. Invert the threshold '''
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

''' Riddler-Calvard method '''
''' Step1. Get the threshold value '''
T = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard threshold: {}".format(T))
''' Step2. Apply the Thresholding value '''
thresh = image.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
''' Step3. Invert the threshold '''
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)

cv2.waitKey(0)