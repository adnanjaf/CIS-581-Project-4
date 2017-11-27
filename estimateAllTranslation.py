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
  from estimateFeatureTranslation import estimateFeatureTranslation 
  
  [row,col]=np.asarray(startXs.shape)
  newXs=np.ones([row,col])
  newYs=np.ones([row,col])
  Ix=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
  Iy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
  gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
  gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
  gradx1=scipy.signal.convolve2d(gray1,Ix,mode='same',boundary='symm')
  grady1=scipy.signal.convolve2d(gray1,Iy,mode='same',boundary='symm')
  gradMap1=np.sqrt(gradx1*gradx1+grady1*grady1)
  gradx2=scipy.signal.convolve2d(gray2,Ix,mode='same',boundary='symm')
  grady2=scipy.signal.convolve2d(gray2,Iy,mode='same',boundary='symm')
  gradMap2=np.sqrt(gradx2*gradx2+grady2*grady2)
  gray1smooth=scipy.ndimage.filters.gaussian_filter(gray1, 5)
  gray2smooth=scipy.ndimage.filters.gaussian_filter(gray2, 5)
  Ix=(gradx1+gradx2)/2
  Iy=(grady1+grady2)/2
  startXs=startXs.astype(int)
  startYs=startYs.astype(int)

  for i in range(col):
      for j in range(row):
          x=startXs[j, i]
          y=startYs[j, i]
          if x==-1:
              break
          else: 
              newx,newy=estimateFeatureTranslation(x,y,Ix,Iy,gray1smooth,gray2smooth)
#              newxGrad,newyGrad=estimateFeatureTranslation(x,y,Ix,Iy,gradMap1,gradMap2)
          newXs[j,i]=newx
          newYs[j,i]=newy
  return newXs, newYs
#  return newXs, newYs