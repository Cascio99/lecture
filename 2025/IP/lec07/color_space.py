import cv2 as cv
import numpy as np

def on_trackbar(pos):
    hmin = cv.getTrackbarPos("H_min","dst")
    hmax = cv.getTrackbarPos("H_max","dst")

    dst = cv.inRange(src_hsv, (hmin,150,0), (hmax,255,255)) # call back function promptly
    cv.imshow('dst', dst)

src = cv.imread("/home/ysw/ws/lecture/2025/IP/lec07/lec7_candies.png", cv.IMREAD_COLOR)
# src = cv.imread("./lec7_candies.png")
src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

dst = cv.inRange(src_hsv, (50,150,0),(80,255,255))

cv.imshow('src', src)
# cv.imshow('dst', dst)
cv.namedWindow('dst')

cv.createTrackbar("H_min", "dst", 50, 179, on_trackbar) # 2nd param: initial value
cv.createTrackbar("H_max", "dst", 80, 179, on_trackbar)


cv.waitKey()
cv.destroyAllWindows()