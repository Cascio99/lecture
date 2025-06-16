import cv2
import numpy as np
from PIL import ImageFont, Image, ImageDraw

# function from hw3
def put_text(img, text, position, font_path, font_size, color):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Convert the frame from BGR to RGB (PIL uses RGB)
    font = ImageFont.truetype(font_path, font_size) # Load the font
    draw = ImageDraw.Draw(img_pil) # Create a drawing context
    draw.text(position, text, font=font, fill=color) # Draw the text
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR) # Convert back to BGR for OpenCV

dir = '/home/ysw/ws/lecture/2025/IP/Data/lec19_Resources/'

ref_img = cv2.imread(dir+'lec19_korea.jpg')
cam = cv2.VideoCapture(dir+'input_201921786.webm')

ar = cv2.VideoCapture(dir+'lec19_korea.mp4')
FPS = 25
duration = 10
frame_cnt = FPS*duration
out = cv2.VideoWriter(dir+'output_201921786.avi', cv2.VideoWriter_fourcc(*'DIVX'), FPS, (1280, 720))

for cnt in range(frame_cnt):
    ret1, cam_frame = cam.read()
    ret2, ar_frame = ar.read()
    if not ret1 or not ret2: break
    # resize the camera frame
    cam_frame = cv2.resize(cam_frame, (1280, 720))
    
    # 1. Keypoint detection and descriptor extraction
    # detector = cv2.KAZE_create()
    detector = cv2.SIFT_create() # more robust than KAZE for this task
    kp1, ref_desc = detector.detectAndCompute(ref_img, None)
    kp2, cam_desc = detector.detectAndCompute(cam_frame, None)
    
    # 2. Matching descriptors
    # matcher = cv2.BFMatcher_create() # used for KAZE
    matcher = cv2.FlannBasedMatcher_create() # KNN matcher(faster than BF in dense descriptors): for SIFT
    matches = matcher.knnMatch(ref_desc, cam_desc, 2)
    good_matches = []
    for m in matches:
        if m[0].distance / m[1].distance < 0.7: # 0.7
            good_matches.append(m[0])
    
    # 3. Homography estimation
    pts1 = np.array([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)
    pts2 = np.array([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2).astype(np.float32)
    H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)
    if H is None:
        print('failed to compute homography at frame', cnt)
        continue

    # debugging
    # dst = cv2.drawMatches(ref_img, kp1, cam_frame, kp2, good_matches, None)
    # (h, w) = ref_img.shape[:2]
    # corner1 = np.array([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2).astype(np.float32)
    # corner2 = cv2.perspectiveTransform(corner1, H)
    # corner2 += np.float32([w, 0])  # Adjusting the corner points to match the scene image
    # cv2.polylines(dst, [np.int32(corner2)], True, (0, 255, 0), 2)
    # cv2.imshow('Matches', dst)

    # 4. Perspective Transformation
    ar_frame = cv2.resize(ar_frame, (ref_img.shape[1], ref_img.shape[0]))
    # warp the ar_frame to the cam_frame
    warped_ar = cv2.warpPerspective(ar_frame, H, (cam_frame.shape[1], cam_frame.shape[0]))
    # mask for the warped_ar
    mask = np.ones(warped_ar.shape, dtype=np.uint8)*255
    warped_mask = cv2.warpPerspective(mask, H, (cam_frame.shape[1], cam_frame.shape[0]))

    # 5. Overlay the warped AR frame on the cam_frame
    cv2.copyTo(warped_ar, warped_mask, cam_frame)   # deep copy

    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf' # if need, sudo apt-get install fonts-nanum*
    cam_frame = put_text(cam_frame, '염선욱 201921786', (50, 40), font_path, 30, (255, 255, 0))
    out.write(cam_frame)
    cv2.imshow('frame', cam_frame)

    key = cv2.waitKey(round(1000/FPS))
    if key == ord('q'):
        break

cam.release()
ar.release()
out.release()