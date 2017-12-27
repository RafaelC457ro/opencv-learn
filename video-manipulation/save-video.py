#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# define codec and create videoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret==True:
        #write frame in file
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
