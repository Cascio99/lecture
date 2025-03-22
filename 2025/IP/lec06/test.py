import cv2 as cv

# Do debugging step by step!!!
# ft. shallow copy vs deep copy

img1 = cv.imread("/home/ysw/ws/25S_lec/IP/lec06/lec6_Resources/lec6_airplane.bmp")
mask = cv.imread("/home/ysw/ws/25S_lec/IP/lec06/lec6_Resources/lec6_airplane_mask.bmp")
img2 = cv.imread("/home/ysw/ws/25S_lec/IP/lec06/lec6_Resources/lec6_field.bmp")

# img2[mask == 255] = img1[mask == 255]
# img1[150:250,150:250] = 128
cv.copyTo(img1, mask, img2)

cv.imshow('img1', img1)
cv.imshow('mask', mask)
cv.imshow('img2', img2)
cv.waitKey(0)
cv.destroyAllWindows()