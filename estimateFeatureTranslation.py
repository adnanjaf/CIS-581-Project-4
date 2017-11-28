'''
  File name: estimateFeatureTranslation.py
  Author:
  Date created:
'''

'''
  File clarification:
    Estimate the translation for single features 
    - Input startX: the x coordinate for single feature wrt the first frame
    - Input startY: the y coordinate for single feature wrt the first frame
    - Input Ix: the gradient along the x direction
    - Input Iy: the gradient along the y direction
    - Input img1: the first image frame
    - Input img2: the second image frame
    - Output newX: the x coordinate for the feature wrt the second frame
    - Output newY: the y coordinate for the feature wrt the second frame
'''

def estimateFeatureTranslation(startX, startY, Ixmap, Iymap, Itmap):
  #TODO: Your code here
  import numpy as np
#  import scipy
  
 
#  Itgrad=img2grad-img1grad
  
#  It=img2-img1
#  centerX=int(startX)
#  centerY=int(startY)
#  It=It[centerY-6:centerY+6,centerX-6:centerX+6]
#  Ix=Ix[centerY-6:centerY+6,centerX-6:centerX+6]
#  Iy=Iy[centerY-6:centerY+6,centerX-6:centerX+6]
#  Itgrad=Itgrad[centerY-6:centerY+6,centerX-6:centerX+6]
#  [row,col]=np.asarray(img1.shape)
#  xlin=np.arange(centerX-6,centerX+6,1)
#  ylin=np.arange(centerY-6,centerY+6,1)
#  xv, yv = np.meshgrid(xlin, ylin, sparse=False, indexing='xy')
#  interFIx=scipy.interpolate.interp2d(xv, yv, Ix, kind='linear')
#  interFIy=scipy.interpolate.interp2d(xv, yv, Iy, kind='linear')
#  interFIt=scipy.interpolate.interp2d(xv, yv, It, kind='linear')
#  interFItgrad=scipy.interpolate.interp2d(xv, yv, Itgrad, kind='linear')
  
  xsamLin=np.arange(startX-5.0,startX+5.0,1.0)
  ysamLin=np.arange(startY-5.0,startY+5.0,1.0)
  IxVal=Ixmap(xsamLin,ysamLin)
  IyVal=Iymap(xsamLin,ysamLin)
  ItVal=Itmap(xsamLin,ysamLin)
#  ItgradVal=interFItgrad(xsamLin,ysamLin)
  
  lfM=np.array([[np.sum(IxVal*IxVal),np.sum(IxVal*IyVal)],[np.sum(IxVal*IyVal),np.sum(IyVal*IyVal)]])
  rtM=np.array([[np.sum(IxVal*ItVal)],[np.sum(IyVal*ItVal)]])
  disp=np.linalg.solve(lfM,-rtM)
  ubright=disp[0,0]
  vbright=disp[1,0]
#  newX=startX+ubright
#  newY=startY+vbright
#  ItVal=Itmap(xsamLin+ubright,ysamLin+vbright)
#  rtM=np.array([[np.sum(IxVal*ItVal)],[np.sum(IyVal*ItVal)]])
#  disp=np.dot(inverse,rtM)
#  ubright=disp[0,0]
#  vbright=disp[1,0]
#  lfMgrad=np.array([[np.sum(IxVal*IxVal),np.sum(IxVal*IyVal)],[np.sum(IxVal*IyVal),np.sum(IyVal*IyVal)]])
#  rtMgrad=np.array([[np.sum(IxVal*ItgradVal)],[np.sum(IyVal*ItgradVal)]])
#  inverse=np.linalg.inv(lfMgrad)
#  disp=np.dot(inverse,-1*rtMgrad)
#  ugrad=disp[0,0]
#  vgrad=disp[1,0]
#  IxVal=interFIx(np.ravel(xv))
#  IyVal=interFIy(np.ravel(xv))
  newX=startX+ubright
  newY=startY+vbright
#  print ubright 
#  print vbright
  return newX, newY