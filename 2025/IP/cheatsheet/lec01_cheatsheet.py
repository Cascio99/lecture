import cv2
import numpy as np

# windows
cv2.namedWindow()
cv2.resizeWindow()
cv2.imshow()
cv2.waitKey() # default: 0
cv2.destroyAllWindows()
cv2.setMouseCallback()

# mouse events
cv2.EVENT_FLAG_LBUTTON
cv2.EVENT_LBUTTONDOWN
cv2.EVENT_LBUTTONUP
cv2.EVENT_FLAG_RBUTTON
cv2.EVENT_FLAG_MBUTTON
...

# trackbars
cv2.createTrackbar()
