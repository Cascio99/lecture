import cv2
import math
import pandas as pd
import os
# 1. 이진화 > 2. 외곽선 검출 > 3. 외곽선 근사화 > 4. 필터링: 크기가 작은 객체와 컨벡스가 아닌 객체 제외 > 5. 도형 종류 판별

DEBUG_MODE = False

shape_to_num = {
    "circle": 0,
    "concave_shape_1": 1,
    "concave_shape_3": 2,
    "ellipse": 3,
    "quadrangle": 4,
    "rectangle": 5,
    "trapezoid": 6,
    "triangle": 7
}

def detect_poly(idx):
    src = cv2.imread(dir + f'image/{idx}.png')
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # Step 1: binarization
    _, img_bin = cv2.threshold(gray, 254, 255, cv2.THRESH_BINARY_INV)
    # Can't identify small objects if use cv2.THRESH_BINARY | cv2.THRESH_OTSU
    # Step 2: find contours
    contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for pts in contours:
        # Step 3: approximate the contour
        approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True) # 0.02
        vertex = len(approx)
        # debugging
        if DEBUG_MODE:
            for p in approx:
                cv2.circle(src, (p[0][0], p[0][1]), 2, (255, 0, 0), -1)

        # Step 4: filter out small objects and non-convex(concave) shapes
        if cv2.contourArea(pts) < 1:
            continue
        if not cv2.isContourConvex(approx):
            if vertex == 4:
                setLabel(src, idx, pts, "concave_shape_1")
            elif vertex == 6:
                setLabel(src, idx, pts, "concave_shape_3")
            continue

        # Step 5: classify the shape
        if vertex == 3:
            setLabel(src, idx, pts, "triangle")

        elif vertex == 4:
            # 1. rectangle?
            is_rect = True
            edges = []
            for i in range(4):
                dx = approx[(i+1)%4][0][0] - approx[i][0][0]
                dy = approx[(i+1)%4][0][1] - approx[i][0][1]
                edges.append((dx, dy))

            for i in range(4):
                dot_product = edges[i][0]*edges[(i+1)%4][0] + edges[i][1]*edges[(i+1)%4][1]
                # at least 1 angle is not 90 degrees
                if abs(dot_product) > 100: # default: 100
                    is_rect = False
                    break

            if is_rect:
                setLabel(src, idx, pts, "rectangle")
                continue
            
            # 2. trapezoid?
            # Check if opposite edges are parallel using inner product
            parallel_pairs = 0
            for i in range(2):
                e1 = edges[i]
                e2 = edges[i + 2]
                dot_product = e1[0]*e2[0] + e1[1]*e2[1]
                mag_e1 = math.sqrt(e1[0]**2 + e1[1]**2)
                mag_e2 = math.sqrt(e2[0]**2 + e2[1]**2)
                in_angle = math.acos(dot_product / (mag_e1*mag_e2))

                # Parallel if angle ≈ 0 or pi (tolerance of 3 degrees)
                if abs(in_angle)<math.radians(3) or \
                abs(in_angle-math.pi)<math.radians(3):
                    parallel_pairs += 1

            if parallel_pairs: # == 1, 2
                setLabel(src, idx, pts, "trapezoid")
                continue
            
            # 3. quadrangle? (parallel pairs == 0)
            setLabel(src, idx, pts, "quadrangle")
            
        else: # circle vs ellipse
            length = cv2.arcLength(pts, True)
            area = cv2.contourArea(pts)
            ratio = 4.*math.pi*area / (length*length)

            if ratio > 0.899: # default: 0.85, test: 0.899
                setLabel(src, idx, pts, "circle")
            else:
                setLabel(src, idx, pts, "ellipse")
    if DEBUG_MODE:
        debugging(src, idx)

def setLabel(img, idx, pts, label):
    # Count the # of shapes
    df.loc[shape_to_num[label], f'img{idx}'] += 1
    # debugging
    if DEBUG_MODE:
        cv2.putText(img, label, (pts[0][0][0], pts[0][0][1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        cv2.drawContours(img, [pts], -1, (0, 0, 0), 1)

def debugging(src, idx): # save image
    out_path = dir + f'contours/{idx}.png'
    if not os.path.exists(os.path.dirname(out_path)):
        os.makedirs(os.path.dirname(out_path))
    cv2.imwrite(out_path, src)

DEBUG_MODE = True
dir = '/home/ysw/ws/lecture/2025/IP/Data/hw6/'
input_path = dir + 'hw6_202200000.xlsx'
output_path = dir + 'hw6_201921786.xlsx'

df = pd.read_excel(input_path, sheet_name='Sheet1', engine='openpyxl')

for idx in range(len(df.columns)-1):
    detect_poly(idx)

df.to_excel(output_path, index=False)

