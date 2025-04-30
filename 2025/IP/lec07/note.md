# Convert color image from ? image to ? image

- opencv2: BGR
- matplotlib: RGB

# Color space
- RGB, BGR, HSV, YUV, YCrCb, Lab, Luv, XYZ, GRAY, ...
- in opencv, img[ , , index:bgr]  # record..
    ## Cons of BGR space: ppt 7 p.
        difficult to filter color like yellow(r+g), cyan(g+b), magenta(b+r)...
        sol) convert color space to HSV
--------
# Caution
    As we use uint8(0~255), we should consider overflow
    i.e. HUE: 0 ~ 360 --> 0 ~ 180

# Cons of BGR: Saturation & Value are not separated (ppt 18 p.)
    HSV: Hue(색상), Saturation(채도), Value(명도)