# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:24:18 2021
@author: Vineet.Srivastava
IMAGE TRANSLATION: Code which will demonstrate shifting the image to 
                   the right or left, Up or Down.
Usage: python imageTranslation.py -i images/trex.png
"""
import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the Image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

#shifts 25 pixels to right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Right and Down", shifted)

#shifts 50 pixels left and 90 pixels Up
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Left and Up", shifted)

#shifts 0 pixels to right and 100 pixels down
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted DOWN", shifted)

cv2.waitKey(0)