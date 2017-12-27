#! /usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('image.png',0)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img)

key = cv2.waitKey(0) & 0xFF

if key == 27:
	cv2.destroyAllWindows()
elif key == ord('s'):
	cv2.imwrite('image-grey.png',img)
	cv2.destroyAllWindows()


