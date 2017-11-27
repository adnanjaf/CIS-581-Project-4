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
  newXs=np.ones([row,col])
  newYs=np.ones([row,col])
  Ix=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
  Iy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
  
#  Ix=np.array([[-1,1],[-1,1]])
#  Iy=np.array([[-1,-1],[1,1]])
  gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
  gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
#  gradx1=cv2.Sobel(gray1,cv2.CV_64F,1,0,ksize=5)
#  abs_gradx1 = np.absolute(gradx1)
#  gradx1 = np.uint8(abs_gradx1)
  gradx1=scipy.signal.fftconvolve(gray1,Ix,mode='same')
  gradx1=gradx1.astype(np.uint8)
  
  grady1=scipy.signal.fftconvolve(gray1,Iy,mode='same')
  grady1=grady1.astype(np.uint8)
#  cv2.imshow('fig2',grady1)
#  cv2.waitKey(0)
#  cv2.destroyAllWindows()
  gradx2=scipy.signal.fftconvolve(gray2,Ix,mode='same')
  gradx2=gradx2.astype(np.uint8)
  grady2=scipy.signal.fftconvolve(gray2,Iy,mode='same')
  grady2=grady2.astype(np.uint8)
  gray1smooth=scipy.ndimage.filters.gaussian_filter(gray1, 5)
  gray2smooth=scipy.ndimage.filters.gaussian_filter(gray2, 5)
#  Ix=(gradx1+gradx2)/2
#  Iy=(grady1+grady2)/2
  Ixmap=gradx1
  Iymap=grady1
  Itmap=gray2-gray1
  ############################
  [ri,ci]=np.asarray(gray1.shape)
  xlin=np.arange(0,ci)
  ylin=np.arange(0,ri)
  interFIx=scipy.interpolate.interp2d(xlin, ylin, Ixmap, kind='linear')
  interFIy=scipy.interpolate.interp2d(xlin, ylin, Iymap, kind='linear')
  interFIt=scipy.interpolate.interp2d(xlin, ylin, Itmap, kind='linear')
  #########################
#  gradx1=scipy.signal.convolve2d(gray1,Ix,mode='same',boundary='symm')
#  grady1=scipy.signal.convolve2d(gray1,Iy,mode='same',boundary='symm')
#  gradMap1=np.sqrt(gradx1*gradx1+grady1*grady1)
#  gradx2=scipy.signal.convolve2d(gray2,Ix,mode='same',boundary='symm')
#  grady2=scipy.signal.convolve2d(gray2,Iy,mode='same',boundary='symm')
#  gradMap2=np.sqrt(gradx2*gradx2+grady2*grady2)
#  gradx1=scipy.ndimage.sobel(gray1, 0)
#  grady1=scipy.ndimage.sobel(gray1, 1)
#  gradMap1=np.hypot(gradx1, grady1)
#  gradx2=scipy.ndimage.sobel(gray2, 0)
#  grady2=scipy.ndimage.sobel(gray2, 1)
#  gradMap2=np.hypot(gradx2, grady2)


#  startXs=startXs.astype(int)
#  startYs=startYs.astype(int)

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