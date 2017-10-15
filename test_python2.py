#_*_ coding:utf-8 _*_
import cv2

img = cv2.imread("/home/ykk/下载/timg.jpeg")
cv2.imshow('image',img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
