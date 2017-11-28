'''
  File name: applyGeometricTransformation.py
  Author:
  Date created:
'''

'''
  File clarification:
    Estimate the translation for bounding box
    - Input startXs: the x coordinates for all features wrt the first frame
    - Input startYs: the y coordinates for all features wrt the first frame
    - Input newXs: the x coordinates for all features wrt the second frame
    - Input newYs: the y coordinates for all features wrt the second frame
    - Input bbox: corner coordiantes of all detected bounding boxes
    
    - Output Xs: the x coordinates(after eliminating outliers) for all features wrt the second frame
    - Output Ys: the y coordinates(after eliminating outliers) for all features wrt the second frame
    - Output newbbox: corner coordiantes of all detected bounding boxes after transformation
'''

def applyGeometricTransformation(startX, startY, newXs, newYs, bbox):
  #TODO: Your code here
  import numpy as np 
  import skimage.transform
  
  
  [row,col]=np.asarray(startX.shape)
  [rb,cb,db]=np.asarray(bbox.shape)
  newbbox=np.zeros([rb,cb,db])
  xlist=[]
  ylist=[]
  numPt=0
  for i in range(col):
      initX=startX[:,i]
      initY=startY[:,i]
      initX=initX[initX!=-1]
      initY=initY[initY!=-1]
      newX=newXs[:,i]
      newY=newYs[:,i]
      newX=newX[newX!=-1]
      newY=newY[newY!=-1]
      
      oldPos=np.matrix.transpose(np.vstack((initX,initY)))
      newPos=np.matrix.transpose(np.vstack((newX,newY)))
      
      t = skimage.transform.SimilarityTransform()
      t.estimate(oldPos, newPos)
      
      coord=np.vstack((initX,initY,np.ones(len(newY))))
      newCoord=np.dot(t.params,coord)
      diff=np.vstack((newX,newY))-newCoord[0:2,:]
      diff=diff*diff
      dist=diff[0,:]+diff[1,:]
#      newX=newX[dist<=16]
#      newY=newY[dist<=16]
      if len(newX)>numPt:
          numPt=len(newX)
      xlist.append(newX)
      ylist.append(newY)
      boxcoord=np.vstack((np.matrix.transpose(bbox[i,:,:]),np.ones(4)))
      newBoxCoord=np.dot(t.params,boxcoord)
      newbbox[i,:,:]=np.matrix.transpose(newBoxCoord[0:2,:])
  Xs=np.ones([numPt,col])*-1
  Ys=np.ones([numPt,col])*-1
  for k in range(col):
      Xs[0:len(xlist[k]),k]=xlist[k]
      Ys[0:len(ylist[k]),k]=ylist[k]
  return Xs,Ys,newbbox