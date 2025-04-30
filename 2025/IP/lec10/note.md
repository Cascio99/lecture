# Point processing, Gamma correction, Histogram equalization
* Transfer Function
i.e. f2: 입력 영상을 밝게 해주는 변환 함수

p 4: 범위 유의해서 clipping(saturation)? 해줘야 함; saturate() or cv2.add()

## 11 p. OX Quiz#1
- 파란색 그래프의 표준편차는 입력영상의 절반이다 (False)
- --> 표준편차: 입력 픽셀들의 밝기 분포에 따라서 달라짐
- alpha=-0.5, 영상 밝기 범위 자체는 절반으로 줄어듦: 명암비는 확실히 줄어듦
- alpha=2: contrast increased

### 13 p. Gamma correction
    - 사람 눈은 어두운 부분에 민감: gamma < 1
    - 반대의 경우(모든 픽셀이 모두 밝아서 질 나쁜 이미지): gamma를 1보다 크게 조정해서 영상의 퀄리티 높임
## 14 p. 시험: 영상처리 전후 비교 및 매칭

## 15 p. Quiz#2(노트)
- 가로축: 밝기(intensity), 세로축: 빈도수(freq), A영상의 histogram ~ gaussian, B 영상 ~ 로그일 때,
- A와 B의 분산 비교: sigma_A < sigma_B

###### opencv functions
    cv2.calcHist()
    matplotlib ~ plt.plot(), plt.show()
    cv2.normalize(); histo_stretching
    cv2.equalizeHist(): histo_eq

### Q) 명압비 보정 방식 2가지?
- hist_stretching, hist_equalization

# Sum) 23 p.
1. 영상 속 픽셀들 간의 "상대적"인 밝기는 불변(invariant)
2. ??? 이해 x  --> 입력영상에서 200이었던 픽셀들은 결과영상에서도 똑같은 값(i.e. 230)라는 뜻
3. src -> Histogram (possible) while Histogram -> src (impossible) due to the lack of spatial_info.