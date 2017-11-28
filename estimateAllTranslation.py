'''
  File name: estimateAllTranslation.py
  Author:
  Date created:
'''

'''
  File clarification:
    Estimate the translation for all features for each bounding box as well as its four corners
    - Input startXs: all x coordinates for features wrt the first frame
    - Input startYs: all y coordinates for features wrt the first frame
    - Input img1: the first image frame
    - Input img2: the second image frame
    - Output newXs: all x coordinates for features wrt the second frame
    - Output newYs: all y coordinates for features wrt the second frame
'''

def estimateAllTranslation(startXs, startYs, img1, img2):
  #TODO: Your code here
  import scipy
  import numpy as np
  import cv2
  import matplotlib.pyplot as plt
  from estimateFeatureTranslation import estimateFeatureTranslation 
  
  [row,col]=np.asarray(startXs.shape)
  newXs=np.ones([row,col])*-1
  newYs=np.ones([row,col])*-1
  Ix=np.array([[1.,0.,-1.],[2.,0,-2.],[1.,0,-1.]])/8.0
  Iy=np.array([[1.,2.,1.],[0,0,0],[-1.,-2.,-1.]])/8.0
  
  gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY).astype(np.double)
  gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY).astype(np.double)
  gradx1=scipy.signal.fftconvolve(gray1,Ix,mode='same')  
  grady1=scipy.signal.fftconvolve(gray1,Iy,mode='same')
  gradx2=scipy.signal.fftconvolve(gray2,Ix,mode='same')
  grady2=scipy.signal.fftconvolve(gray2,Iy,mode='same') 
  gray1smooth=scipy.ndimage.filters.gaussian_filter(gray1, 1)
  gray2smooth=scipy.ndimage.filters.gaussian_filter(gray2, 1)
  Ixmap=(gradx1+gradx2)/2.0
  Iymap=(grady1+grady2)/2.0
  Itmap=gray2smooth-gray1smooth
  ############################
  [ri,ci]=np.asarray(gray1.shape)
  xlin=np.arange(0,ci)
  ylin=np.arange(0,ri)
  interFIx=scipy.interpolate.interp2d(xlin, ylin, Ixmap, kind='linear')
  interFIy=scipy.interpolate.interp2d(xlin, ylin, Iymap, kind='linear')
  interFIt=scipy.interpolate.interp2d(xlin, ylin, Itmap, kind='linear')
  #########################

  for i in range(col):
      for j in range(row):
          x=startXs[j, i]
          y=startYs[j, i]
          if x==-1:
              break
          else: 
              newx,newy=estimateFeatureTranslation(x,y,interFIx,interFIy,interFIt)
          newXs[j,i]=newx
          newYs[j,i]=newy
  return newXs, newYs