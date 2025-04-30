import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
# ddpeth = -1, dx = 1, dy = 0, ksize = 3
dx = cv2.Sobel(src, -1, 1, 0)
dst = cv2.Sobel()
cv2.normalize()

cv2.magnitude()
cv2.phase()

cv2.Canny(src, threshold1=100, threshold2=200, apertureSize=3, L2gradient=True)
# apertureSize: kernel size
# L2gradient
  # True: use L2 norm to calculate gradient magnitude
  # False: use L1 norm to calculate gradient magnitude