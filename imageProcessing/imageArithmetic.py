# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:09:18 2021

@author: Vineet.Srivastava

Usage: python imageArithmetic.py -i images/trex.png
"""
from __future__ import print_function
import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

''' Adding 100 to each pixel - increases brightness'''
M = np.ones(image.shape, dtype = "uint8") * 100
added = cv2.add(image, M)
cv2.imshow("Added", added)

''' Substracting 50 from each pixel of image - decreases brightness'''
M = np.ones(image.shape, dtype = "uint8") * 50
substracted = cv2.subtract(image, M)
cv2.imshow("Substracted", substracted)

cv2.waitKey(0)