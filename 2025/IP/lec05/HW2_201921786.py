import cv2 as cv

cap1 = cv.VideoCapture("/home/ysw/ws/lecture/2025/IP/lec05/lec5_Resources/lec5_video1.mp4")
cap2 = cv.VideoCapture("/home/ysw/ws/lecture/2025/IP/lec05/lec5_Resources/lec5_video2.mp4")

w = round(cap1.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = cap1.get(cv.CAP_PROP_FPS)
fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps)
out = cv.VideoWriter('/home/ysw/ws/lecture/2025/IP/lec05/HW2_201921786.avi', fourcc, fps, (w, h))
# print("FPS: ", fps) # 24
# print("w, h: ", w, h)

cnt = 0
while(cap1.isOpened()):
    cnt += 1
    # print('cnt: ', cnt)
    ret1, frame1 = cap1.read()
    
    if cnt >= fps:
        ret2, frame2 = cap2.read()
        if not ret2:
            break

    if cnt < fps:   
        out.write(frame1)
        # cv.imshow('frame', frame1)
    elif cnt >= fps and cnt < 3*fps:
        col = round((cnt - fps) * w / (2*fps))
        frame1[:,:col,:] = frame2[:,:col,:]
        out.write(frame1)
        # cv.imshow('frame', frame1)
    else:
        out.write(frame2)
        # cv.imshow('frame', frame2)
    cv.waitKey(delay)

cap1.release()
cap2.release()
out.release()
