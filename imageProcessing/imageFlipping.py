# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:07:09 2021

@author: Vineet.Srivastava

Utility to flip the images 
Usage: python imageFlipping.py -i images/trex.png
"""
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

''' Flipping image horizontally - flipping around y-axis'''
flipped = cv2.flip(image, 2)
cv2.imshow("Flipped Horizontally", flipped)

''' Flipping image vertically - flipping around x-axis'''
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

''' Flipping image horizontally as well as vertically'''
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)

cv2.waitKey(0)