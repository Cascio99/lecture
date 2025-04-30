# Arithmetic operation
- 255보다 큰 픽셀은 255로 설정(saturation: 포화); clamping(어떤 위치를 범위 안으로 한정)
- dst(x,y) = saturate(src1(x,y) + src2(x,y))
- cv2.addWeighted(src1, alpha, src2, beta, gamma, dst=None, dtype=None) → dst
- cv2.subtract(src1, src2, dst=None, mask=None, dtype=None) → dst
- dst(x,y) = |src1(x,y) - src2(x,y)|
- cv2.absdiff(src1, src2, dst=None) → dst

# Logical operation
- cv2.bitwise_and(src1, src2, dst=None, mask=None)
- cv2.bitwise_or(), .._xor(), .._not()