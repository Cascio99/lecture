import cv2
import numpy as np

# create a image data
# np.empty()  |
# np.zeros()  |    -> type: numpy.ndarray
# np.ones()   |
# np.full()   |

img1 = np.zeros((512, 512, 3), dtype=np.uint8)   # black image
# deep copy
img2 = cv2.copyTo(img1, None)
# shallow copy
img3 = img1

img2[100:400, 100:400] = 128
img3.fill(255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()