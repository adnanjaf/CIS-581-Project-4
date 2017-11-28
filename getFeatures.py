'''
  File name: getFeatures.py
  Author:
  Date created:
'''

'''
  File clarification:
    Detect features within each detected bounding box
    - Input img: the first frame (in the grayscale) of video
    - Input bbox: the four corners of bounding boxes
    - Output x: the x coordinates of features
    - Output y: the y coordinates of features
'''

def getFeatures(img, bbox):
  #TODO: Your code here
    import numpy as np
    import cv2
    import scipy
    from skimage.feature import corner_shi_tomasi,corner_harris
    #img=cv2.imread('many.jpg')
    #bbox=detectFace.detectFace(img)
#    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    [row,col,dim]=np.asarray(bbox.shape)
    bbox=bbox.astype(int)
    neighbors=np.ones((3,3))
    xcoord=[]
    ycoord=[]
    numPt=0
    for i in range(row):
        currentFace=img[bbox[i,0,1]:bbox[i,2,1],bbox[i,0,0]:bbox[i,1,0]]
        currentFace=corner_harris(currentFace)
        idx=(currentFace>0.05)
        currentFace=currentFace*idx
        localM=scipy.ndimage.filters.maximum_filter(currentFace,footprint=neighbors)
        msk=(currentFace==localM)
        msk=msk*currentFace
        [y,x]=np.where(msk>0)
        x=x+bbox[i,0,0]
        y=y+bbox[i,0,1]
        if len(x)>numPt:
            numPt=len(x)
        xcoord.append(x)
        ycoord.append(y)
    #    for k in range(len(x)):
    #        cv2.circle(gray,(x[k],y[k]),5,(0,0,255),1)
    x=np.ones((numPt,row))*-1
    y=np.ones((numPt,row))*-1
    for k in range(row):
        x[0:len(xcoord[k]),k]=xcoord[k]
        y[0:len(ycoord[k]),k]=ycoord[k]
    return x,y
#cv2.imshow('fig1',gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

