import cv2
import numpy as np

cv2.imread()
cv2.imwrite()
cap = cv2.VideoCapture()

cap.get(propId=) # propId=5 for fps
cap.set(propId=, value=)
cap.isOpened()

out = cv2.VideoWriter()
ret, frame = cap.read()
out.write(frame)

cap.release()
out.release()


    # About indexing order
# opencv uses row-major order: (x_2, x_1) = (row, column)
# others(numpy, list, etc) uses column-major order: (x_1, x_2) = (row, column)

# opencv uses BGR order
# numpy(numpy, list, etc) uses RGB order