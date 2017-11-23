# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:37:24 2017

@author: zoue
"""

import numpy as np 
import cv2 
import scipy 
import matplotlib.pyplot as plt
from detectFace import detectFace
from getFeatures import getFeatures
from IPython import get_ipython
from estimateAllTranslation import estimateAllTranslation
from estimateFeatureTranslation import estimateFeatureTranslation
from applyGeometricTransformation import applyGeometricTransformation


frameSet=[]
video=cv2.VideoCapture('MarquesBrownlee.mp4')
tf= True 

while tf:
    tf,frame=video.read()
    frameSet.append(frame)
    
frameSet=frameSet[:-1]
bbox=detectFace(frameSet[0])
gray=cv2.cvtColor(frameSet[0],cv2.COLOR_BGR2GRAY)
x,y=getFeatures(gray,bbox)
newXs,newYs =estimateAllTranslation(x,y,frameSet[0],frameSet[1])
para=applyGeometricTransformation(x,y,newXs,newYs,bbox)

#plt.imshow(grad, cmap='gray')
#cv2.imshow('fig1',frameSet[0])
#cv2.waitKey(0)
#cv2.destroyAllWindows()