# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 01:18:26 2018

@author: Pankaj
"""

import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--img", type = str, required=True)
args = parser.parse_args()

image=cv2.imread(args.img)
# image=imutils.resize(image,width=1000)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces=face_cascade.detectMultiScale(gray_img,1.2,5)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow('img_haar',image)
cv2.waitKey(0)
