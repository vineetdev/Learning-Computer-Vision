# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:44:15 2021

@author: Vineet.Srivastava
About: Demonstrates Histogram Equalization. 
       It improves contrast in a picture.
Usage: python imageHistEqualize.py -i images/beach.png 
"""

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to Image File")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
#cv2.imshow("Original Image", image)

''' Convert image to gray '''
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

''' Prform Histogram Equalization '''
eq = cv2.equalizeHist(image)
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))

cv2.waitKey(0)