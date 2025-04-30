import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('/home/ysw/ws/lecture/2025/IP/lec13_2/EXR/lec13_Resources/lec12_dial.jpg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(gray, (5, 5), 0.5)
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 50, param1=120, param2=50, minRadius=20, maxRadius=50)

if circles is not None:
    for i in range(circles.shape[1]):
        cx,cy,radius = np.uint16(circles[0][i])
        cv2.circle(src, (cx, cy), radius, (0, 255, 0), 2)

cv2.imshow('src', src)
cv2.waitKey(0)