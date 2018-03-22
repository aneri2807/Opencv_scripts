import numpy as np
import cv2

img = cv2.imread('panda.jpg', cv2.IMREAD_COLOR)

#opencv BGR blue green red
cv2.line(img,(0,0),(150,150), (255,255,255), 15)
cv2.rectangle(img,(15,25),(200,150),(255,0,0),5)
cv2.circle(img , (100,70),45,(0,0,255),-1)

pts = np.array([[10,3],[20,20],[50,30],[50,25],[10,90]])
#pts=pts.reshape((-1,1,2))
#reshape to 1*2 array not necessary
cv2.polylines(img , [pts],True,(0,255,0),3)
#true to state if yopu want to connect last and first pt


font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'ANERI @',(100,100),font,1,(200,140,200),4,cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
