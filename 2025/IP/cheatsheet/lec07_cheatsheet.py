import cv2
import numpy as np

src = np.full((512, 512, 3), 255, dtype=np.uint8)   # white image
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
cv2.inRange(src, lowerb=np.ndarray, upperb=np.ndarray)

cv2.split(src, output)   # split BGR to B, G, R
cv2.merge()   # merge B, G, R to BGR