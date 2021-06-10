# -*- coding: utf-8 -*-
"""
Created on Mon May 31 17:22:09 2021

@author: Vineet.Srivastava
"""
from __future__ import print_function 
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# Lets change one pixel color of image
#(b, g, r) = image[0,0]
#print("Pixel at (0,0) - Red: {}, Green:{}, Blue:{}".format(r, g, b))
(b, g, r) = image[219,90]
print("Pixel at (219,90) - Red: {}, Green:{}, Blue:{}".format(r, g, b))


image[0,0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0,0) - Red: {}, Green:{}, Blue:{}".format(r, g, b))
cv2.imshow("Changed Image", image)

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)
cv2.imshow("Changed Corner", image)

print("Changed corner color")
cv2.waitKey(0)