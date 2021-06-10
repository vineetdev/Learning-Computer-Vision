# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:38:51 2021
@author: Vineet.Srivastava
Utility for Image Translation which will be used in imageTranslation.py file
Usage: will be used internally by imageTranslation.py file
"""
import numpy as np
import cv2

''' Utility function to translate/shift a image to right/left/top/down '''
def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

''' Utility function to rotate a image by given angle around given center '''
def rotate(image, angle, center = None, scale = 1.0):
    (h, w) = image.shape[:2]
    
    if center is None:
        center = (w // 2, h // 2)
        
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

''' Utility function to resize the image by giving desired width or height '''
def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    dim = None
    (h,w) = image.shape[:2]
    
    if width is None and height is None :
        return image
    
    if width is None:
        r = height / float(h)
        dim = (int(w*r), height)
    else:
        r = width / float(w)
        dim = (width, int(h*r))
        
    resized = cv2.resize(image, dim, interpolation = inter)
     
    return resized

''' Utility function to get contours irrespective of the OpenCV version '''
def grab_contours(cnts):
    if len(cnts) == 2:
        cnts = cnts[0]
    elif len(cnts) == 3:
        cnts = cnts[1]
    else:
        raise Exception(("Contours tuple must have length 2 or "
                         "3, otherwise OpenCV changed their cv2.findContours"
                         "return signature yet again. "
                         "Refer to OpenCV's documentation in that case "))
    return cnts

