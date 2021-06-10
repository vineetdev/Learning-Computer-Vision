# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:23:22 2021

@author: Vineet.Srivastava
About: Demonstrates drawing of color histograms for B, G and R
       Multi-dimensional Color Histograms taking two channels at  a time.
Usage: python imageHistColors.py -i images/beach.png
"""
from matplotlib import pyplot as plt
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to Image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

''' Color Histograms for all the channels B, G and R'''
chans = cv2.split(image)
colors = ("b", "g", "r")

plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

for (chan, color) in zip(chans, colors):
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
    plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)

''' Multi dimensional color histograms using AND '''
''' Multi dimensional color histograms for G and B '''
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([chans[1], chans[0]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)
plt.show()
cv2.waitKey(0 )

''' Multi dimensional color histograms for G and R '''
fig = plt.figure()
ax = fig.add_subplot(132)
hist = cv2.calcHist([chans[1], chans[2]], [0, 1], None,
                    [8, 8], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)
plt.show()
cv2.waitKey(0)

''' Multi dimensional color histograms for B and R '''
fig = plt.figure()
ax = fig.add_subplot(133)
hist = cv2.calcHist([chans[0], chans[2]], [0, 1], None,
                    [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation = "nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
plt.show()

print("2D histogram shape: {}, with {} values".format(hist.shape, 
                                        hist.flatten().shape[0]))

cv2.waitKey(0)

