# Hough transform part1. Line detection
- intro) 영상에 직선이 한 개일 때는 least_sqare 방식으로 (a,b) 찾을 수 있지만,
- 두 개 이상일 때는 허프변환으로 (a_k,b_k) 찾아야 됨
- key idea: image domain(x,y) -> parameter domain(a,b)
- param_domain에서 직선이 교차(중첩)하면 pixel cnt

## param_domain's range...
- a, b의 범위에 제한 없는데, Cart_coord??
- sol) Cart_Coord (x, y) --> Polar_Coord (rho, theta)

## cv2.HoughLinesP(): improved v. of cv2.HoughLines()
