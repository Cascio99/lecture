import cv2
import numpy as np
import matplotlib.pyplot as plt

# lec11 ~: consider neighboring pixels while ~ lec10: point transformation

# Frequency domain filtering: FFT and IFFT
# Spatial domain filtering (ft. weight kernel/mask)
    # linear filtering
cv2.filter2D(src, ddepth=cv2.CV_8U, kernel, anchor, delta, borderType)
        # 최외각 픽셀 처리 (padding)
cv2.BORDER_CONSTANT # 0
cv2.BORDER_REPLICATE
cv2.BORDER_REFLECT
...

    # Image blurring (= smoothing)
        # 1. Box filtering (= mean filtering)
cv2.blur(src, ksize)
        # 2. Gaussian filtering
cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
        # 3. Median filtering (non-linear)
cv2.medianBlur(src, ksize)
        # 4. Bilateral filtering (non-linear, edge-preserving)
cv2.bilateralFilter(src, diameter=, sigmaColor, sigmaSpace, borderType)