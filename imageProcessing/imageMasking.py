# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:42:46 2021

@author: Vineet.Srivastava
Demonstrates usage of mask on an image using opencv
Usage: python imageMasking.py -i images/beach.png
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

''' Define a Rectangular mask '''
mask = np.zeros(image.shape[:2], dtype = "uint8")
(cx, cy) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (cx - 75, cy - 75), (cx + 75, cy + 75), 255, -1)
cv2.imshow("Mask", mask)

''' Apply mask to the image '''
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Masked", masked)
cv2.waitKey(0)

''' Define a circular mask '''
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cx, cy), 100, 255, -1)
cv2.imshow("Circular Mask", mask)

''' Apply the circular mask to the image '''
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Circular Masked", masked)
cv2.waitKey(0)
