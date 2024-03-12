import cv2 as cv
import numpy as np
img8=cv.imread("7.jpg")
img8=cv.resize(7,(400,500))
img9=cv.imread("8.jpg")
img9=cv.resize(10,(400,500))
img10=np.hstack([img8,img9])
cv.imwrite("img8.jpg",img8)
