# == 1차 미분 필터, Edge Detection ==

# 1st order filter (8 p.)
- Prewitt, Sobel, Scharr ~ (smoothing + derivative)
### Prewitt filter: 고주파 노이즈 약간 있..
- sol) Gaussian smoothing, LPF 적용한 후 미분(Prewitt filter)
- Quiz) Box filtering에서 normalize 필요 없는 이유는?
- Ans) 상대적인 intensity 차이가 중요하기 때문
### Sobel filter ~ gauissian filtering `[1, 2, 1]`
Q) prewitt-x도 세로방향의 에지 검출하는 필터인지? ㅇㅇ (모든 1차 미분 필터에 적용)
- `Seperable filter`: 3 * 3 filter를 3 * 1과 1 * 3으로 쪼갤 수 있는 필터: 계산량 감소 효과
### Scharr filter
- smoothing filter: [3, 10, 3]


# Other filters
    - Derivative of Gaussian
    - Gabor
    - Laplacian
    - Difference of Gaussian

## Gradient
#### Derivative of Gaussian: 앞의 1차 필터와 달리 parameter(표준편차, 분산 등) 조정 가능
- 사람의 개입이 들어간다고 더 좋다는 건 아님
#### Gabor filtering: 2D Gaussian + Sinusoidal func(19 p.)
- Gabor filter "bank": 모든 각도 적용해서 나온 output 합치기
- 사람의 적극 개입; lambda, sigma, theta, gamma, psi

## 2nd order filter
- 자주 쓰진 않음
- zero-crossing
- LoG: Laplacian of Gaussian ~= Difference of Gaussian ( no need to compute derivative)



## Edge-Detection process (25 p.)
1. Select a derivative filter (i.e. Sobel)
2. Linear filtering (i.e. convolution)
3. Compute gradient (amp & direction)
4. Binarization




# Canny edge detection (26 ~ 33 p.)
    - ****** 30 p. *******
    - 단일 경계를 찾기 위한 에지 검출기(하나의 에지)
    - consider ONLY closed-loop objects, not open..
1. Gaussian filtering (optional)
2. Calculate gradient by Sobel-filter
3. NMS(Non-maximum suppression)
    - gradient가 local-max인 `단일 엣지(픽셀)`만 표현 (gradient 방향으로의 주변 2개의 픽셀 비교): 두꺼웠던 엣지를 얇게 만듦
4. Hysteresis thresholding (double threshold) --> 29 p.
    - gradient magnitude를 기준으로 double-thresholding
    - |f| : NMS로 검출한 에지들의 gradient magnitude
    - 강한 에지: |f| ≥ T_high
    - 약한 에지: T_low ≤ |f| ≤ T_high -> 강한 에지와 연결되어 있는 픽셀만 에지로 지정