# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:22:00 2021

@author: Vineet.Srivastava

Utility to resize the images
Usage: python imageResize.py -i images/trex.png
"""
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

''' aspect ratio of image needs to be maintained while resizing image'''

""" Resize the image to new width 150 """
''' ratio of new width 150 with old width of image '''
r = 150.0 / image.shape[1]

''' new dimensions of image '''
dim = (150, int(image.shape[0]*r))

''' algorithm for resizing image is INTER_AREA to get best result 
    while resizing the image'''
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized Image New Width 150", resized)
print(" width 150 new height {}".format(resized.shape[0]))

""" Resize the image to new height 110 """
r = 110.0 / image.shape[0]
dim = (int(image.shape[1]*r), 110)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized Image New Height 110", resized)
print(" height 110 new width {}".format(resized.shape[1]))

""" Resize the image to new width 200 """
resized = imutils.resize(image, width = 900)
cv2.imshow("Width 200", resized)

cv2.waitKey(0)