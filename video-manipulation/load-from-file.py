#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture('assets/683855647.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.imshow('frame', frame)

        cv2.namedWindow('gray', cv2.WINDOW_NORMAL)
        cv2.imshow('gray', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
