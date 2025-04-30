import cv2 as cv

# Debug step by step!!!
# ft. shallow copy vs deep copy

# mask 원리 이해(ft. line17)
# out = cv.copyTo(img1, mask, img2)에서
# img1의 "mask == 255인 부분(픽셀)"을 img2에 복사
# mask == 255인 부분을 ROI(Region of Interest)라고 함

img1 = cv.imread("/home/ysw/ws/lecture/2025/IP/lec06/lec6_Resources/lec6_airplane.bmp")
mask = cv.imread("/home/ysw/ws/lecture/2025/IP/lec06/lec6_Resources/lec6_airplane_mask.bmp")
img2 = cv.imread("/home/ysw/ws/lecture/2025/IP/lec06/lec6_Resources/lec6_field.bmp")

# img2[mask == 255] = img1[mask == 255]
# img1[150:250,150:250] = 128
out = cv.copyTo(img1, mask, img2)   # deep copy

# shallow copy
test = img1 
test[150:250,150:250] = 128
cv.imshow('img1', img1)
cv.imshow('test', test)

# cv.imshow('img1', img1)
# cv.imshow('mask', mask)
cv.imshow('img2', img2)
# cv.imshow('out', out)

while (True):
    key = cv.waitKey(0)
    if key == 27: # ESC key
        cv.destroyAllWindows()
        break