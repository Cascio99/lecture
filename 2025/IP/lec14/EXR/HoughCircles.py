import cv2 as cv
import numpy as np

src = cv.imread('/home/ysw/ws/lecture/2025/IP/lec14/EXR/lec13_Resources/lec12_dial.jpg')

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(gray, (5, 5), 0.5)

circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, 50, param1=120, param2=50, minRadius=20, maxRadius=50)
# minR=5, maxR=50
# threshold 올리면 원이 덜 검출됨(param2: 10 -> 50)

if circles is not None:
    for i in range(circles.shape[1]):
        cx,cy,radius = np.uint16(circles[0][i])
        cv.circle(src, (cx, cy), radius, (0, 255, 0), 2)

cv.imshow('src', src)
cv.waitKey(0)