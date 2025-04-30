import cv2
import numpy as np
import matplotlib.pyplot as plt

# Point processing: dst(x,y) <- f(src(x,y)), f: transfer function

# Change brightness of image: dst(x,y) <- saturate(src(x,y)+n)
src1 = np.ones((300, 300), dtype=np.uint8) * 100
src2 = np.ones((300, 300), dtype=np.uint8) * 100
    # 1. cv2.add()
dst1 = cv2.add(src1, src2)
    # 2. 사칙연산 후 uint8형으로 변환: np.clip().astype()
dst2 = np.clip(src1+155., 0, 255).astype(np.uint8)

cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)

# Contrast(명암비: 밝기 차이): represented by pixels' (intensity) variance
    # dst(x,y) <- saturate(s*src(x,y))
    #     VS
    # dst(x,y) <- saturate(src(x,y) + (src(x,y)-128)*alpha)
# Prob#1) 11 p. Compare alpha=-0.5, 2
    #--> 그래프(x: in, y: out)으로 이해!

# Gamma correction: I_out = I_in^gamma
    # gamma < 1 VS gamma > 1
    # cf. gamma_Eyes < 1 ~= log ==> 사람의 눈은 어두운 부분에서 더 민감함.
    # gamma ∝ 1/contrast ?

# Histogram: 대표적인 명암비의 정량적인 평가지표 -> quality improvement of image
hist1 = cv2.calcHist([src1], [0], None, [256], [0, 256])
    # hist_stretching
hist2 = cv2.normalize(src1, None, 0, 255, cv2.NORM_MINMAX)
    # hist_equalization(평활화): 전체 구간에서 균일한 분포
    # hist_CDF와의 관계: 26 p.
hist3 = cv2.equalizeHist(src1)

cv2.imshow('hist3', hist3)

plt.plot(hist1)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()