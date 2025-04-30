import numpy as np
import cv2 as cv

# img = np.zeros((512,512,3), np.uint8)

# img = cv.line(img, (0,0), (511,511), (255,0,0), 5)
# img = cv.rectangle(img, (384,0), (510,128), (0,255,0), 3)
# img = cv.circle(img, (447,63), 63, (0,0,255), -1)

# cv.putText(img, 'OpenCV', (100,400), cv.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 2)

img = cv.imread('/home/ysw/ws/lecture/2025/IP/lec04/lec4_vehicles.jpg', cv.IMREAD_COLOR) # image -> numpy.ndarray
        
img = cv.rectangle(img, (100,100), (200,300), (0,255,0), 3)

cv.imwrite('/home/ysw/ws/lecture/2025/IP/lec04/HW1_201921786.jpg', img) # numpy.ndarray -> image

cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
