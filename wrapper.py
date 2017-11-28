# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:37:24 2017

@author: zoue
"""

import numpy as np 
import cv2 
import scipy 
import matplotlib.pyplot as plt
import matplotlib
from detectFace import detectFace
from getFeatures import getFeatures
from estimateAllTranslation import estimateAllTranslation
from applyGeometricTransformation import applyGeometricTransformation


frameSet=[]
newFrameSet=[]
video=cv2.VideoCapture('TheMartian.mp4')
tf= True 

while tf:
    tf,frame=video.read()
    frameSet.append(frame)
    
frameSet=frameSet[:-1]

bbox=detectFace(frameSet[0])
gray=cv2.cvtColor(frameSet[0],cv2.COLOR_BGR2GRAY)
x,y=getFeatures(gray,bbox)


#drawing
plt.imshow(cv2.cvtColor(frameSet[0], cv2.COLOR_BGR2RGB))
[r1b,c1b,d1b]=np.asarray(bbox.shape)
for i in range(r1b):
    b=bbox[i,:,:]
    xloc=x[:,i]
    yloc=y[:,i]
    facebb=matplotlib.patches.Polygon(b,closed=True,fill=False)
    features=plt.plot(xloc,yloc,'w.',ms=1)
    plt.gca().add_patch(facebb)
    #plt.fig(bbox_inches='tight',pad_inches=0)
plt.axis('off')
plt.savefig("temp.png",dpi=300,bbox_inches="tight")
img=cv2.imread("temp.png")
plt.close()
newFrameSet.append(img);

#getting features and transforming 
for k in range(1,15):
    newXs,newYs =estimateAllTranslation(x,y,frameSet[k-1],frameSet[k])
    Xs,Ys,newbbox=applyGeometricTransformation(x,y,newXs,newYs,bbox)
    plt.imshow(cv2.cvtColor(frameSet[k], cv2.COLOR_BGR2RGB))
    print len(Xs)
    for j in range (r1b):
        b=newbbox[j,:,:]
        xloc=Xs[:,j]
        yloc=Ys[:,j]
        facebb=matplotlib.patches.Polygon(b,closed=True,fill=False)
        features=plt.plot(xloc,yloc,'w.',ms=1)
        plt.gca().add_patch(facebb)
    plt.axis('off')
    plt.savefig("temp.png",dpi=300,bbox_inches="tight")
    img=cv2.imread("temp.png")
    plt.close()
    newFrameSet.append(img);
    x=Xs
    y=Ys
    bbox=newbbox
    
    
[height,width,layer]=np.asarray(newFrameSet[0].shape)
outPut=cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'MP4V'),5,(width,height))
for m in range (len(newFrameSet)):
    outPut.write(newFrameSet[m].astype('uint8'))
    cv2.destroyAllWindows()
outPut.release()

    
#plt.imshow(grad, cmap='gray')
#cv2.imshow('fig1',frameSet[0])
#cv2.waitKey(0)
#cv2.destroyAllWindows()