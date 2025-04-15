import cv2 as cv
import numpy as np
from PIL import ImageFont, Image, ImageDraw

img1 = cv.imread('/home/ysw/ws/lecture/2025/IP/lec09/lec9_field.bmp', cv.IMREAD_COLOR)
img2 = cv.imread('/home/ysw/ws/lecture/2025/IP/lec09/lec9_airplane.bmp', cv.IMREAD_COLOR)

FPS = 30
duration = 5    # seconds
frame_cnt = FPS * duration

out = cv.VideoWriter('/home/ysw/ws/lecture/2025/IP/lec09/hw4_201921786.avi', cv.VideoWriter_fourcc(*'DIVX'), FPS, (img1.shape[1], img1.shape[0]))

# from hw3...
def put_text(img, text, position, font_path, font_size, color):
    img_pil = Image.fromarray(cv.cvtColor(img, cv.COLOR_BGR2RGB))   # Convert the frame from BGR to RGB (PIL uses RGB)

    font = ImageFont.truetype(font_path, font_size) # Load the font

    draw = ImageDraw.Draw(img_pil)  # Create a drawing context
    
    draw.text(position, text, font=font, fill=color)    # Draw the text

    return cv.cvtColor(np.array(img_pil), cv.COLOR_RGB2BGR) # Convert back to BGR for OpenCV

for cnt in range(frame_cnt):
    font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  # Make sure this path is correct

    if cnt/FPS < 1:
        dst = img1
    elif cnt/FPS >= 1 and cnt/FPS < 4:
        dst = cv.addWeighted(img1, 1-(cnt/FPS-1)/3, img2, (cnt/FPS-1)/3, 1)
    else:
        dst = img2

    dst = put_text(dst, '201921786 염선욱', (20, 15), font_path, 25, (255, 255, 0))    # yellow: R+G
    cv.imshow('frame', dst)
    out.write(dst)
    
    key = cv.waitKey(round(1000/FPS))   # delay := round(1000/FPS)
    if key == ord('q'):
        break

out.release()
cv.destroyAllWindows()