import cv2 as cv

cap = cv.VideoCapture("/home/ysw/ws/25S_lec/IP/lec05/lec5_Resources/lec5_video2.mp4")
cap2 = cv.VideoCapture("/home/ysw/ws/25S_lec/IP/lec05/lec5_Resources/lec5_video1.mp4")

w = round(cap.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv.CAP_PROP_FPS)
fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps)
out = cv.VideoWriter('/home/ysw/ws/25S_lec/IP/lec05/lec5_video2_out.avi', fourcc, fps, (w, h))
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

    # frame[100:200,:,:] = 255
    if cnt < fps:
        inversed = frame
    else:
        inversed = ~frame
    out.write(inversed)
    cv.imshow('frame', frame)
    cv.imshow('inversed', inversed)
    cv.waitKey(delay)

cap.release()
cap2.release()
out.release()