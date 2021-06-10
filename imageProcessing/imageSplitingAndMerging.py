# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 13:40:53 2021

@author: Vineet.Srivastava
Demonstrates spliting a image into different channels 
and finally merging the splitted channels back into original image

Usage: python imageSplitingAndMerging.py -i images/wave.png
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

''' Splitting image into different channels '''
(B, G, R) = cv2.split(image)
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

''' Merge the splitted channels to make final image '''
merged = cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

''' To show seperate channels in picture in color '''
zeros = np.zeros(image.shape[:2], dtype = "uint8")
cv2.imshow("RedChannel", cv2.merge([zeros, zeros, R]))
cv2.imshow("GreenChannel", cv2.merge([zeros, G, zeros]))
cv2.imshow("BlueChannel", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)