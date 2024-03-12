import cv2 as cv
import numpy as np
img1=cv.imread("3.jpg")
img1=cv.resize(img1,(200,300))
img2=cv.imread("4.jpg")
img2=cv.resize(img2,(200,300))
img4=np.hstack([img1,img2])
cv.imwrite("Img4.jpg",img4)
