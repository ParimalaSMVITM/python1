import cv2 as cv
import numpy as np
img1=cv.imread("1.jpg")
img1=cv.resize(img1,(200,300))
img2=cv.imread("2.jpg")
img2=cv.resize(img2,(200,300))
img3=cv.imread("3.jpg")
img3=cv.resize(img3,(200,300))
img4=np.hstack([img1,img2,img3])
cv.imwrite("Img6.jpg",img4)
