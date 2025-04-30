import cv2
import numpy as np
src1 = np.full((3, 3), dtype=np.uint8)
src2 = np.ndarray((3, 3), dtype=np.uint8)

# Arithmetic operations
# 포화(Saturation) 연산
dst <- saturate(src1(x,y) + src2(x,y))

dst1 = cv2.addWeighted(src1, alpha, src2, beta, gamma)
dst2 = cv2.subtract(src1, src2, dst=None, mask=None, dtype=None)
# dst3 <- |src1(x,y) - src2(x,y)|
dst4 = cv2.absdiff(src1, src2, dst=None)

# Logical operations
dst5_1 = cv2.bitwise_and(src1, src2, dst=None, mask=None)
dst5_2 = cv2.bitwise_or(src1, src2, dst=None, mask=None)
dst5_3 = cv2.bitwise_xor(src1, src2, dst=None, mask=None)
dst5_4 = cv2.bitwise_not(src1, dst=None, mask=None)

# [mask 원리 이해]
# out = cv.copyTo(img1, mask, img2)에서
# img1의 "mask == 255인 부분(픽셀)"을 img2에 복사
# mask == 255인 부분을 ROI(Region of Interest)라고 함
