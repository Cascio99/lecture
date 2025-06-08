import cv2 # (downward, rightward) order
import numpy as np
# sudo apt install tesseract-ocr libtesseract-dev tesseract-ocr-kor
# pip install pytesseract
import pytesseract

# *이진화 -> *외곽선 검출 -> 다각형 근사화 -> *투시 변환 -> OCR

def order_points(pts): # pts: (4, 2)
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1) # (x+y)
    rect[0] = pts[np.argmin(s)] # 좌상
    rect[2] = pts[np.argmax(s)] # 우하

    diff = np.diff(pts, axis=1) # (y-x)
    rect[1] = pts[np.argmin(diff)] # 우상
    rect[3] = pts[np.argmax(diff)] # 좌하
    return rect

dir = '/home/ysw/ws/lecture/2025/IP/Data/hw7/'
src = cv2.imread(dir+'lec17_namecard1.jpg') # lec17_namecard2.jpg
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
h, w = gray.shape[:2]
TYPE = 1 if h*w < 1e7 else 2 # namecard1 vs namecard2

# I. Locally Adaptive Thresholding #1: 조명 보정 후 전역 이진화(Otsu)
# 1. Surface Fitting
# 좌표 평면 생성 (x, y 좌표)
X, Y = np.meshgrid(np.arange(w), np.arange(h))
A = np.c_[X.flatten(), Y.flatten(), np.ones(h*w)] # (1555200, 3)
z = gray.flatten() # (1555200, 1)

# 평면의 계수 (a, b, c) 추정: ax + by + c = z by least squares
(a, b, c), _, _, _ = np.linalg.lstsq(A, z, rcond=None) # solve Ax = z

# 평면 조명 성분
illumApprox = (a*X + b*Y + c).reshape(h, w).astype(np.uint8)

# 2. Shading Compensation
compensated = cv2.subtract(gray, illumApprox) # original - approximation

# 3. 전역 이진화: Otsu
_, binary = cv2.threshold(compensated, 0, 255, cv2.THRESH_OTSU)
binary = cv2.GaussianBlur(binary, (5, 5), 10) # (4, 1, 2)

# II. findContours
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
for pts in contours:
    # III. approximate the contour: 0.02
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    # 꼭짓점이 4개가 아니거나, arcLenth가 1000 미만인 경우 제외
    # print(len(approx), cv2.arcLength(approx, True)) # 4, 1712 for namecard1.jpg
    if len(approx) != 4 or cv2.arcLength(approx, True) < 1000:
        continue
    tmp = src.copy()
    cv2.drawContours(tmp, [approx], -1, (0, 255, 0), 2)

    # IV. perspective transform
    src_ = approx.reshape(4, 2).astype('float32')
    src_ = order_points(src_) # 좌상, 우상, 우하, 좌하 순서로 정렬
    dst_ = np.array([[0, 0], [720, 0], [720, 400], [0, 400]], dtype='float32')
    # Homography matrix 계산
    H = cv2.getPerspectiveTransform(src_, dst_)
    dst = cv2.warpPerspective(src, H, (720, 400))

    # V. OCR
    ocr = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
    fsize = 2 if TYPE == 1 else 3.5
    ocr = cv2.resize(ocr, None, fx=fsize, fy=fsize, interpolation=cv2.INTER_CUBIC)
    text = pytesseract.image_to_string(ocr, lang='kor+eng', config='--psm 6 --oem 1 --dpi 600')
    print(text)
    with open(dir+f'ocr_result_{TYPE}.txt', 'w') as f:
        f.write(text)
    
cv2.imshow('src', src)
cv2.imshow('binary', binary)
if tmp is not None: cv2.imshow('contour', tmp)
if dst is not None: cv2.imshow('dst', dst)
cv2.waitKey(0)

cv2.imwrite(dir+f'binary_{TYPE}.png', binary)
cv2.imwrite(dir+f'contour_{TYPE}.png', tmp)
cv2.imwrite(dir+f'dst_{TYPE}.png', dst)