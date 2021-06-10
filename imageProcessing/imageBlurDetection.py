# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 12:03:46 2021

@author: Vineet.Srivastava
This will detect blur in images.
Usage: python imageBlurDetection.py --images images
"""
from imutils import paths
import argparse
import cv2 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required = True,
                help = "Path to input directory of images")
ap.add_argument("-t", "--threeshold", type = float, default = 100.0,
                help = "focus measures that fall below this value will be considered 'blurry'")
args = vars(ap.parse_args())

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus measure,
    # which is simply the variance of Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

# Loop over all the images
for imagePath in paths.list_images(args["images"]):
    # Read each image
    image = cv2.imread(imagePath)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Calculate the variance of Laplacian
    fm = variance_of_laplacian(gray)
    
    # This text will be added to the image file
    text = "Not Blurry"
    
    if(fm < args["threeshold"]):
        text = "Blurry"
        
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    key = cv2.waitKey(0)
    
cv2.waitKey(0)
