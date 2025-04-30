# Hough Transf part 2: circle
- EXR) HoughCircles(): `원의 중심 먼저` 찾고 `반지름을 검출`하는 Hough gradient method 사용
- 여러 개의 동심원을 검출하지는 못함

### Hough Gradient Method
    (x-a)^2 + (y-b)^2 == r^2 에서 3차원 param-domain은 너무 복잡해서
    2차원 공간도메인에서 먼저 edge 검출 후
    edge에서 gradient 방향으로 직선 누적해서 원의 중심 예측
    
##### HW5
    실제 원과 얼마나 가까운지를 평가함.
    타원은 제외.
    정확하게 원만 카운트.
    엑셀 파일 입출력 및 저장 기능: Pandas 참고
    제출 파일: hw5_201921786.py, hw5_201921786.xlsx