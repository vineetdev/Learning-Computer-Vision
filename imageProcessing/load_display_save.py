# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:24:59 2021
@author: Vineet.Srivastava
Usage: python load_display_save.py --image ../images/trex.png
"""

from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image file")
args = vars(ap.parse_args())

"""Load image file"""
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

"""Display the image"""
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.imwrite("displayedImage.jpg", image)