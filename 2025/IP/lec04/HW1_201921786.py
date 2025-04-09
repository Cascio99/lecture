import cv2 as cv

img = cv.imread('/home/ysw/ws/lecture/2025/IP/lec04/lec4_vehicles.jpg', cv.IMREAD_COLOR)

def draw(event, x, y, flags, param):
    global ix, iy

    if event == cv.EVENT_LBUTTONDOWN:
        ix, iy = x, y
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(img, (ix, iy), (x, y), (255,0,0), 3)

    elif event == cv.EVENT_MBUTTONDOWN:
        cv.circle(img, (x, y), 5, (0,0,255), -1)

    cv.imshow('image', img)

cv.imshow('image', img)

cv.setMouseCallback('image', draw)

while True:
    key = cv.waitKey(1)
    if key == ord('q'):
        cv.imwrite('/home/ysw/ws/lecture/2025/IP/lec04/HW1_201921786.jpg', img)
        cv.destroyAllWindows()
        break
