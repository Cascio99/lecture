import cv2 as cv
import numpy as np
from PIL import ImageFont, Image, ImageDraw

# Debug step by step!!!
# ft. shallow copy vs deep copy

fg = cv.VideoCapture("/home/ysw/ws/lecture/2025/IP/lec06/lec6_Resources/lec6_woman.mp4")
bg = cv.VideoCapture("/home/ysw/ws/lecture/2025/IP/lec06/lec6_Resources/lec6_raining.mp4")

w = round(fg.get(cv.CAP_PROP_FRAME_WIDTH))
h = round(fg.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = fg.get(cv.CAP_PROP_FPS)
fourcc = cv.VideoWriter_fourcc(*'DIVX')
delay = round(1000/fps)
out = cv.VideoWriter('/home/ysw/ws/lecture/2025/IP/lec06/hw3_201921786.avi', fourcc, fps, (w, h))

def show_hsv(event, x, y, flags, param):    # debug
    if event == cv.EVENT_LBUTTONDOWN:
        hsv_frame = cv.cvtColor(param, cv.COLOR_BGR2HSV)
        hsv_value = hsv_frame[y, x]
        print(f'HSV at ({x}, {y}): {hsv_value}')

def put_text(img, text, position, font_path, font_size, color):
    img_pil = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))   # Convert the frame from BGR to RGB (PIL uses RGB)

    font = ImageFont.truetype(font_path, font_size) # Load the font

    draw = ImageDraw.Draw(img_pil)  # Create a drawing context
    
    draw.text(position, text, font=font, fill=color)    # Draw the text

    return cv.cvtColor(np.array(img_pil), cv.COLOR_RGB2BGR) # Convert back to BGR for OpenCV

cnt = 0
flag = False
while(fg.isOpened()):
    ret1, frame1 = fg.read()
    if not ret1:
        break

    # cv.putText(frame1, '201921786 염선욱', (50,50), font, 1, (0,255,255), 2)
    # cv.putText(frame1, f'Chroma key mode: {on_off}', (50,100), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    # cv.putText(frame1, f'Frame id: {cnt}', (50,150), cv.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
    # korean text is not supported in cv2.putText()

    on_off = 'ON' if flag else 'OFF'
    # if need, sudo apt-get install fonts-nanum*
    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # Make sure this path is correct
    frame1 = put_text(frame1, '201921786 염선욱', (50, 40), font_path, 30, (255, 255, 0))    # yellow: R+G
    frame1 = put_text(frame1, f'Chroma key mode: {on_off}', (50, 80), font_path, 30, (255, 255, 0))
    frame1 = put_text(frame1, f'Frame id: {cnt}', (50, 120), font_path, 30, (255, 255, 0))

    key_input = cv.waitKey(delay)
    if key_input == ord(' '):
        flag = not flag
    elif key_input == ord('q'):
        break

    if flag:    # chroma key mode
        cnt += 1
        
        ret2, frame2 = bg.read()
        if not ret2:
            flag = False
            continue    # if bg video is shorter than fg video, loop bg video
            # break

        hsv = cv.cvtColor(frame1, cv.COLOR_BGR2HSV)
        GREEN_MIN = (45, 100, 100)
        GREEN_MAX = (65, 255, 255)
        # mask: green area -> black, non-green area -> white
        mask = ~cv.inRange(hsv, GREEN_MIN, GREEN_MAX)   # fg(woman, text): white, bg(raining): black
        cv.imshow('mask', mask)

        cv.copyTo(frame1, mask, frame2) # deep copy
        cv.imshow('frame2', frame2)
        out.write(frame2)
    else:   # normal mode
        cv.imshow('frame1', frame1)
        cv.setMouseCallback('frame1', show_hsv, frame1) # debug
        out.write(frame1)

fg.release()
bg.release()
out.release()
cv.destroyAllWindows()