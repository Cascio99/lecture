import cv2 as cv
import numpy as np

src = cv.imread('/home/ysw/ws/lecture/2025/IP/lec13_2/EXR/lec13_Resources/lec12_dial.jpg')
# iris: 600*257
# dial: 500*491

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
img_blur = cv.GaussianBlur(gray, (5, 5), 0.5)
# cv2.HOUGH_GRADIENT에서는 p.s. Canny 안 쓰는 이유?
    # circle: 곡선 + 얇은 엣지.
        # 그런데 Canny를 쓰면:
        # 엣지가 너무 얇거나 끊어져서 나오거나
        # 약한 곡선들이 다 끊겨버릴 수도 있음.

circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, 50, param1=120, param2=50, minRadius=20, maxRadius=50)
# minR=5, maxR=50
# threshold 올리면 원이 덜 검출됨(param2: 10 -> 50)
# param2_dial: 50, param2_iris: 40

# param2=10, minR=1, maxR=50
# image: input image
# method: cv2.HOUGH_GRADIENT
# dp: 입력 영상 대비 축적배열의 크기 비율
# minDist: 검출된 원 중심점들의 최소거리
# param1: T_high in canny edge detection
# param2: 축적 배열에서 원 검출을 위한 임계값
# minRadius, maxRadius: 검출할 원의 최소/최대 반지름 길이

if circles is not None:
    for i in range(circles.shape[1]):
        cx,cy,radius = np.uint16(circles[0][i])
        cv.circle(src, (cx, cy), radius, (0, 255, 0), 2)

# cv.imshow('gray', gray)
# cv.imshow('img_blur', img_blur)

print(circles.shape[1])

cv.imshow('src', src)
cv.waitKey(0)