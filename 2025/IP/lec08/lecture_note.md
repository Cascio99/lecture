# Image Data (ppt lecture_8)
- photo-diode: convert 'light' into 'electric signal'
- ISP: low level processor
- Pin-hole camera: mathematical model (blackbox, )
`estimate distance by focal length, ...`
## 6 p
- electrical signal (밝기): continuous --> too much computation (wrt time, memory)
- how to extract discrete # of signals(input)?
- sol) sampling by quantization(3-bit{0~7} for 6 p)
* uint8(8-bit): 0 ~ 255
- 8 p: 광량(밝기: intensity) 조절하기 위해선 조리개, 셔터 속도 조절 필요
- horizontal_fov(M), v_fov(N) --> M, N이 클수록 resolution 높은 것
- grayscale (1 channel) vs color image (3 channel)
- channel: matrix # wrt depth (intensity)