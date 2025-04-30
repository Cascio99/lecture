import cv2 as cv

cap = cv.VideoCapture("/home/ysw/ws/lecture/2025/IP/lec05/lec5_Resources/lec5_video2.mp4")
cap2 = cv.VideoCapture("/home/ysw/ws/lecture/2025/IP/lec05/lec5_Resources/lec5_video1.mp4")

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH)) # 1280
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) # 720
fps = cap.get(cv.CAP_PROP_FPS)  # propId=5 for fps
# fps = cap.get(propId=5)
fourcc = cv.VideoWriter_fourcc(*'DIVX') # compression method(codec)
delay = round(1000/fps)
out = cv.VideoWriter('/home/ysw/ws/lecture/2025/IP/lec05/lec5_video2_out.avi', fourcc, fps, (w, h))
print("delay: ", delay) # 42
print("FPS: ", fps) # 24

cnt = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    ret2, frame2 = cap2.read()
    if ret2 == True:
        frame[:,300:,:] = frame2[:,300:,:]
    cnt += 1

    frame[100:200,:,:] = 255
    if cnt < fps:
        inversed = frame
    else:
        inversed = ~frame
    out.write(inversed)
    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)
    if cv.waitKey(delay) == 27: # ESC key
        break

cap.release()
cap2.release()
out.release()