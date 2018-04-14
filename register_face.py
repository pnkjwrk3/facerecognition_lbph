# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:41:00 2018

@author: Pankaj
"""

import cv2
import sqlite3
import numpy as np
import os

# connect database
conn = sqlite3.connect('usersdatabase.db')
c = conn.cursor()

if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

# load cascade classifier file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
u_name = input("Enter your name: ")
c.execute('INSERT INTO users (name) VALUES (?)', (u_name,))
uid = c.lastrowid
sampleNum = 0

while True:
  _,img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in faces:
    sampleNum = sampleNum+1
    cv2.imwrite("dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.waitKey(100)
  cv2.imshow('img',img)
  cv2.waitKey(1);
  if sampleNum > 25: #capture 25 images of the face from webcam
    break

cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()
