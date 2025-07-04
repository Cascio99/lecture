import cv2
import numpy as np

src = cv2.imread("/home/ysw/ws/lecture/2025/IP/Data/lec16_Resources/lec16_keyboard.bmp", cv2.IMREAD_GRAYSCALE)

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src_bin, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt):
    (x,y,w,h,area) = stats[i]
    if area < 20:
        continue

    cv2.rectangle(dst, (x, y, w, h), (0,255,255))

cv2.imshow("src", src)
cv2.imshow("src_bin", src_bin)
cv2.imshow("dst", dst)
cv2.waitKey(0)






