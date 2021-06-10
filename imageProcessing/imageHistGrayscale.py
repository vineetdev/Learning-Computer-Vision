# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:07:04 2021

@author: Vineet.Srivastava
Demonstrates how Histogram can be plotted for a image using matplotlib and OpenCV
Usage: python imageHistGrayscale.py -i images/beach.png
"""
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

''' Gray out the image '''
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", image)

''' Calculate the Histogram '''
hist = cv2.calcHist([image], [0], None, [256], [0,256])

'''Generate the plot'''
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins") # Bins are plotted on x-axis
plt.ylabel("# of Pixels") # Number of pixels in each bin are plotted on y-axis
plt.plot(hist)
plt.xlim([0,256])
plt.show()

cv2.waitKey(0)
