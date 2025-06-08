import cv2 as cv
import numpy as np
import pandas as pd
import os
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html

def cnt_circles(idx):
    src = cv.imread(dir + f'images/{idx}.png')

    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(gray, (5, 5), 0.5)
    # minDist: 50->100, param2=10->30, minR=20, maxR=50->80
    circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, 100, param1=120, param2=30, minRadius=20, maxRadius=80)
    # threshold for ... param1: Canny, param2: Accum_array

    debugging(circles, src, idx)
    return circles.shape[1]

def debugging(circles, src, idx):
    if circles is not None:
        print(f"{idx}th image has", circles.shape[1], "circles")
        for i in range(circles.shape[1]):
            cx,cy,radius = np.uint16(circles[0][i])
            cv.circle(src, (cx, cy), radius, (0, 0, 255), 2)
    
    out_path = dir + f'hough_images/{idx}.png'
    if not os.path.exists(os.path.dirname(out_path)):
        os.makedirs(os.path.dirname(out_path))
    
    if circles.shape[1] == 0:
        print(f"***No Circles in {idx}th image!***")
    cv.imwrite(out_path, src)

dir = '/home/ysw/ws/lecture/2025/IP/Data/hw5/'
input_path = dir + 'circle_counter.xlsx'
output_path = dir + 'hw5_201921786.xlsx'

# pip install openpyxl
df = pd.read_excel(input_path, sheet_name='Sheet1', engine='openpyxl')

for idx in range(len(df)):
    res = cnt_circles(idx)
    df.loc[idx, 'predicted_circle'] = res

df.to_excel(output_path, index=False)
