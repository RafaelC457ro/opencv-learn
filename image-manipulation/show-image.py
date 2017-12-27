#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as ptl

img = cv2.imread('image.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('test',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
