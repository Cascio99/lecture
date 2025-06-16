import cv2
import numpy as np

dir = '/home/ysw/ws/lecture/2025/IP/Data/lec19_Resources/'

src1 = cv2.imread(dir + 'lec19_book.png', cv2.IMREAD_GRAYSCALE)
src2 = cv2.imread(dir + 'lec19_book_in_scene.png', cv2.IMREAD_GRAYSCALE)

# Keypoint detection and descriptor extraction using KAZE
detector = cv2.KAZE_create()
kp1, desc1 = detector.detectAndCompute(src1, None)
kp2, desc2 = detector.detectAndCompute(src2, None)

# Matching descriptors using BFMatcher
matcher = cv2.BFMatcher_create()
matches = matcher.match(desc1, desc2)
matches = sorted(matches, key=lambda x: x.distance)
good_matches = matches[:50]

# Homography estimation
pts1 = np.array([kp1[m.queryIdx].pt for m in good_matches])\
    .reshape(-1, 1, 2).astype(np.float32)
pts2 = np.array([kp2[m.trainIdx].pt for m in good_matches])\
    .reshape(-1, 1, 2).astype(np.float32)
H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
# Homography based Perspective Transformation
if H is None: 
    print("Homography could not be computed.")
    exit()
dst = cv2.drawMatches(src1, kp1, src2, kp2, good_matches, None)

(h, w) = src1.shape[:2]
corner1 = np.array([[0,0], [0,h-1], [w-1,h-1], [w-1,0]]).reshape(-1, 1, 2).astype(np.float32)
corner2 = cv2.perspectiveTransform(corner1, H)
# corner2 += (w, 0)  # Adjusting the corner points to match the scene image
corner2 += np.float32([w, 0])  # Adjusting the corner points to match the scene image
cv2.polylines(dst, [np.int32(corner2)], True, (0, 255, 0), 2)
# need to tranform 

cv2.imshow('Matches', dst)
cv2.waitKey(0)