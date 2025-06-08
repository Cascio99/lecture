import cv2

src = cv2.imread('/home/ysw/ws/lecture/2025/IP/lec14/lec14_cells.png', cv2.IMREAD_GRAYSCALE)

def on_threshold(pos):
    threshold = cv2.getTrackbarPos('Threshold', 'dst')
    # _, dst = cv2.threshold(src, threshold, 100, cv2.THRESH_BINARY)
    _, dst = cv2.threshold(src, threshold, 255, cv2.THRESH_BINARY_INV)
    # how to remove noise blobs? : morphological operation (next lecture)
    # how to set threshold? : Otsu's method

    cv2.imshow('dst', dst)

cv2.imshow('src', src)
cv2.namedWindow('dst')
cv2.createTrackbar('Threshold', 'dst', 0, 255, on_threshold)
cv2.setTrackbarPos('Threshold', 'dst', 127)

cv2.waitKey(0)
cv2.destroyAllWindows()