
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
