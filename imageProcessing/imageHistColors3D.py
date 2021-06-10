# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:11:48 2021
@author: Vineet.Srivastava
About: Demonstrate 3D Color Histogram
Usage: python imageHistColors3D.py -i images/beach.png
"""
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import argparse
import cv2 

''' Set the argument parses '''
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the Image File")
ap.add_argument("-s", "--size", required = False,
                help = "Size of largest color bin", default = 5000)
ap.add_argument("-b", "--bins", required = False,
                help = "Number of bins per color channel", default = 8)
args = vars(ap.parse_args())

''' Parse the incoming values '''
image = cv2.imread(args["image"])
size = float(args["size"])
bins = int(args["bins"])

''' Calculate the Histogram '''
hist = cv2.calcHist([image], [0, 1, 2], None, 
                    [bins, bins, bins], [0, 256, 0, 256, 0, 256])

print("3D Histogram shape: %s, with %d values" % (
    hist.shape, hist.flatten().shape[0]))

''' Lets visualize the 3D Histogram '''
fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ratio = size / np.max(hist)

for(x, plane) in enumerate(hist):
    for(y, row) in enumerate(plane):
        for(z,col) in enumerate(row):
            if hist[x][y][z] > 0.0:
                siz = ratio * hist[x][y][z]
                rgb = (z/(bins - 1), y/(bins - 1), x/(bins - 1))
                ax.scatter(x, y, z, s = siz, facecolors = rgb)
plt.show()

cv2.waitKey(0)