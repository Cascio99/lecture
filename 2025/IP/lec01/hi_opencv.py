import numpy as np
import cv2 as cv
print(cv.__version__)

def onMouse(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print("Left button pressed", (x, y))
    elif event == cv.EVENT_RBUTTONDOWN:
        print("Right button pressed", (x, y))
        
def onChange(val):
    global img, title
    img[:] = val
    cv.imshow(title, img)


img = np.full((300, 500), 255, np.uint8) # default: np.uint8
# img = np.zeros((300, 500), np.uint8)
# img[:] = 100
title = 'window'
cv.imshow(title, img)

cv.setMouseCallback(title, onMouse)

cv.createTrackbar('Brightness', title, 100, 255, onChange)

cv.waitKey()
cv.destroyAllWindows()

# img = np.zeros((200,400), np.uint8)
# img[:] = 200

# title1, title2 = 'Position1', 'Position2'
# cv.namedWindow(title1, cv.WINDOW_AUTOSIZE)
# cv.namedWindow(title2)
# print("???")
# cv.moveWindow(title1, 150, 150)
# cv.moveWindow(title2, 400, 50)


# cv.imshow(title1, img)
# cv.imshow(title2, img)
# cv.waitKey(0)
# cv.destroyAllWindows()