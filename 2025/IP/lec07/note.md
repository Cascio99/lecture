# Mar 27(Thu) 휴강

# convert color image from ? image to ? image

# opencv2: BGR
# matplotlib: RGB

# color space: RGB, BGR, HSV, YUV, YCrCb, Lab, Luv, XYZ, GRAY, ...

# in opencv, img[?:,?:,index:bgr]  # record..
    # Cons) ppt 7 p.
    # difficult to filter color like yellow(r+g), cyan(g+b), magenta(b+r)...

    # sol) convert color space to HSV

####################### [Caution] #######################
# because we use uint8(0~255), we should consider overflow
# --> hue: 0 ~ 360 -> 0 ~ 180

# Cons of BGR: Saturation & Value are not separated (ppt 18 p.)
    # HSV: Hue, Saturation, Value