import numpy as np
import cv2

img = cv2.imread('panda.jpg', cv2.IMREAD_COLOR)

#px = img[55,55]

#print(px)->color val fr the px
img[55,55]=[255,255,255]
px = img[55,55]
##roi = img[100:150, 100:150]
##print(roi)
#region of img ->roi
img[100:150, 100:150] = [255,255,255]

pandii = img[37:111, 107:194]
img[0:74,0:87] = pandii
# 107-37=74,194-111
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
