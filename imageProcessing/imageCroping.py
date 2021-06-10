# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 17:36:15 2021

@author: Vineet.Srivastava
This file demonstrates Image cropping
Usage: python imageCroping.py -i images/trex.png
"""

import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                      help = "Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

''' Lets crop the image using NumPy array slicing '''
''' OpenCV represents images as NumPy arrays with height first and 
    width second '''
cropped = image[30:120, 240:335]
cv2.imshow("T-rex face", cropped)

cv2.waitKey(0)