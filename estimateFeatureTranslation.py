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
  xsamLin=np.arange(startX-5.0,startX+5.0,1.0)
  ysamLin=np.arange(startY-5.0,startY+5.0,1.0)
  IxVal=Ixmap(xsamLin,ysamLin)
  IyVal=Iymap(xsamLin,ysamLin)
  ItVal=Itmap(xsamLin,ysamLin)
  
  lfM=np.array([[np.sum(IxVal*IxVal),np.sum(IxVal*IyVal)],[np.sum(IxVal*IyVal),np.sum(IyVal*IyVal)]])
  rtM=np.array([[np.sum(IxVal*ItVal)],[np.sum(IyVal*ItVal)]])
  disp=np.linalg.solve(lfM,-rtM)
  ubright=disp[0,0]
  vbright=disp[1,0]
  
  newX=startX+ubright
  newY=startY+vbright
  
#  k=1
#  while k<=5:
#       xsamLin=np.arange(newX-5.0, newX+5.0,1.0)
#       ysamLin=np.arange(newY-5.0, newY+5.0,1.0)
#       ItVal=Itmap(xsamLin,ysamLin)
#       rtM=np.array([[np.sum(IxVal*ItVal)],[np.sum(IyVal*ItVal)]])
#       disp=np.linalg.solve(lfM,-rtM)
#       ubright=disp[0,0]
#       vbright=disp[1,0]
#       newX=newX+ubright
#       newY=newY+vbright
#       k=k+1
#       if (ubright*ubright+vbright*vbright)<0.001:
#           break
       
  return newX, newY