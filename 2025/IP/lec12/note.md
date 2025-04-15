# 6 p. ~ 1st order filter 웬만하면 암기?(별로 없음); 물리적 의미
## Prewitt filter: 고주파 노이즈 약간 있..
- sol) gaussian smoothing, LPF 적용한 후 미분(Prewitt filter)
- Quiz)`box filtering에서 normalize 필요 없는 이유는?`
## Sobel filter ~ gauissian filtering
Q) prewitt-x도 세로방향의 에지 검출하는 필터인지? ㅇㅇ
- `Seperable filter`: 3*3 filter를 3*1과 1*3으로 쪼갤 수 있는 필터
## Scharr filter

### opencv func
- cv2.Sobel(), cv2.normalize()

* 세로방향의 엣지 찾으려면 sobel filter의 어느 축으로 미분해야 하는가?  (x축)

## Gradient
- 
### opencv func
- cv2.magnitude(), cv2.phase()
## DoG: 앞의 1차 필터와 달리 parameter(표준편차, 분산 등) 조정 가능
- 사람의 개입이 들어간다고 더 좋다는 건 아님
## Gabor filtering: 2D Gaussian + Sinusoidal func(19 p.)
- gabor filter "bank": 모든 각도의 gabor filter 모두 적용해서 나온 output 합치기
- 사람의 적극 개입 많음; lambda, sigma, theta, gamma, psi

======================================
# 2nd order filter
- 자주 쓰진 않음
- zero-crossing
- laplacian filter(a / b in 22 p.)
- LoG: Laplacian of Gaussian
## Summary in 25 p.
- edge detection by step1~4
======================
# Canny edge detection: 26 ~ 33 p.
- 단일 경계를 찾기 위한 에지 검출기(하나의 엦)
- ...
- step3: NMS(Non-maximum suppression): `단일 엣지(픽셀)`만 표현
- step4: Hysteresis thresholding(double threshold)
### opencv func
- cv2.Canny()