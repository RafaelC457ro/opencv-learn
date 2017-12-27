#! /usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# mouse callback function
def draw_cicle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),10,(255,0,0),-1)

#create black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_cicle)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
