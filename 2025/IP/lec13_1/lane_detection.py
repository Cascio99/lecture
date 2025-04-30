import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('/home/ysw/ws/lecture/2025/IP/lec13_1/lec13_Resources/lec12_lanes.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 200) # Canny edge detection

# Hough Transform
lines = cv.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(img, (x1, y1), (x2, y2), (0, 255, 255), 2) # Draw lines on the original image

# plt.imshow(img[:,:,::-1])
# plt.axis('off')
# plt.show()
cv.imshow('win',img)
cv.imshow('edges', edges)
cv.waitKey(0)