import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lec12_lanes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200) # Canny edge detection

# Hough Transform
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=50, minLineLength=50, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 2) # Draw lines on the original image

# cv2.imshow('win',img)