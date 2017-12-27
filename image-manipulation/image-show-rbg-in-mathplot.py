#! /usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('image.png')

b,g,r = cv2.split(img)
img2  = cv2.merge([r,g,b])

plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(img2)

plt.show()




