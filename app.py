# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# imggambar= cv2.imread("download.jpg",1)
# cv2.imshow('hasil',imggambar)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# height, width = imggambar.shape[:2]
# qheight, qwidth = height / 4, width / 4
# T = np.float32([[1, 0, qwidth], [0, 1, qheight]])
# img_translation = cv2.warpAffine(imggambar, T, (width, height))
# tampil_hor=np.concatenate((imggambar,img_translation),axis=1)
# cv2.imshow('hasil',tampil_hor)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# imgmedian = cv2.medianBlur(imggambar,15)
# tampil_hor=np.concatenate((imggambar,imgmedian),axis=0)
# cv2.imshow('hasil',tampil_hor)
# cv2.waitKey(0)
# cv2.destroyAllWindows

import cv2
import matplotlib
import numpy as np
from matplotlib import pyplot as plt

imggambar= cv2.imread("china.jpg",0)
thresh = 150

img_binary = cv2.threshold(imggambar, thresh, 255, cv2.THRESH_BINARY)[1]
tampil_hor=np.concatenate((imggambar,img_binary),axis=1)

cv2.imshow('hasil',tampil_hor)
cv2.waitKey(0)
cv2.destroyAllWindows
