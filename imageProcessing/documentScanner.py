# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:53:25 2021

@author: Vineet.Srivastava
Usage: python documentScanner.py -i images/doc.png
"""
from skimage.filters import threshold_local
from imageTransform import four_point_transform
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to Image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original Image", image)

# Compute the ratio of old height to new height, make a copy and resize it
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

# Convert the image to grayscale, blur it and find the edges
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

# Show the edged image
cv2.imshow("EDGED", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Find the contours, sort them
cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

# Check whether we got the 4 edges for the rectangle
found = False
for c in cnts:
    peri = cv2.arcLength(c, True) # get the perimeter
    approx = cv2.approxPolyDP(c, 0.02*peri, True) # Approximate it to closed Rectangle
    
    if len(approx) == 4:
        screenCnt = approx
        found = True
        print("Found Document")
        break
    
if found == True:
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("OUTLINED", image)
else:
    cv2.imshow("NOT FOUND", image)
    print("Document not found")
    
# apply the four point transform to obtain a top-down
# view of the original image
print("screencnt:{}".format(screenCnt))
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

# convert the warped image to grayscale, then threshold it
# to give it that 'black and white' paper effect
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8") * 255

# show the original and scanned images
print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.waitKey(0)

cv2.waitKey(0)