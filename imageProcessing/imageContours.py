# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 18:33:41 2021

@author: Vineet.Srivastava
About: Demonstrates getting contours from image
Usecase: Counting number of coins in image
Usage: python imageContours.py -i images/coins.png
"""
from __future__ import print_function 
import numpy as np
import argparse 
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path for Image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

''' perform edges detection on image '''
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edged", edged)

''' From the edges get the count of contours '''
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, 
                             cv2.CHAIN_APPROX_SIMPLE)

print("cnts {}".format(cnts))
print("I found {} coins in image".format(len(cnts)))

''' Draw contours in original image '''
coins = image.copy() # take a copy of image and work on it
''' Green color with thickness of 2 is chosen for the contours drawn '''
''' We can draw Contours either over all coins or on coins one by one '''
#cv2.drawContours(coins, cnts, -1, (0, 255, 0), 2)
#cv2.imshow("Coins", coins)

# We can also draw contours over the individual coins with the below example
cv2.drawContours(coins, cnts, 0, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.drawContours(coins, cnts, 1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)

''' Lets crop each coin from the image '''
for (i, c) in enumerate(cnts):
    # Find the enclosing box in which the coin will fit in
    (x,y,w,h) = cv2.boundingRect(c)
    print("Coin #{}".format(i+1))
    
    ''' Crop the coin from the image '''
    coin = image[y:(y + h), x:(x + w)]
    cv2.imshow("Coin", coin)
    
    ''' Lets fit a circle to the coin '''
    mask = np.zeros(image.shape[:2], dtype = "uint8")
    ((centerX, centerY), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(centerX), int(centerY)), int(radius), 255, -1)
    
    mask = mask[y:y+h, x:x+w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask = mask))
    cv2.waitKey(0)

cv2.waitKey(0)
