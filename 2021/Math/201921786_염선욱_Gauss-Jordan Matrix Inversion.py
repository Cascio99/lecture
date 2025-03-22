#고성능 계산이 가능한 패키지인 numpy는 외부 라이브러리이므로 따로 설치해줘야 한다.
#https://pypi.org/project/numpy/#files 1. 위 사이트에서 운영체제(32비트/64비트)와 Python버전을 비교해 설치받는다
#2.cmd를 열어서 "python -m pip install 파일 위치\파일"을 실행해서 설치한다.

import numpy as np                                      #numpy 라이브러리 포함하는 명령문
#AB=I에서 IB=B로 바꾸는 함수 정의(B is inverse of A)
#parameter(매개변수) A(Coefficient Matrix)와 I(Identity Matrix)의 변화에 집중
def G_J_M_I(A,I):
    #Array A,I 선언(data type: real)
    A = np.array(A, float)
    I = np.array(I, float)
    n = len(I)                                          #n: row 개수  
    #i가 0부터 (n-1)th column까지 1씩 증가하며 iterate
    for i in range(n):        
        #diagonal element가 0인 경우에만 row끼리 바꾸는 작업
        if np.fabs(A[i,i]) == 0:                        #A[i,i] component의 절댓값이 0이면...
            for z in range(i+1,n):                      #같은 col 속에서 0 아닌 원소를 가지는 row 찾기
                if np.fabs(A[z,i]) > np.fabs(A[i,i]):   #zth row 찾았으면...
                    for x in range(i, n):                #0 가지는 ith row와 0 아닌 원소 가지는 xth row 위치 교환
                        A[i,x],A[z,x] = A[z,x],A[i,x]
                    I[i],I[z] = I[z],I[i]               #Identity Matrix도 동일하게 Row끼리 위치 바꾸기
                    break                
        #해당 coloumn에 있는 모든 row element를 1로 바꾸기
        diagon = A[i,i]                                 #diagonal element 변수 선언
        for j in range(i,n):                            
            A[i,j] /= diagon                            #위에서 아래로 내려오면서(j를 1씩 증가) 모든 성분들을 1로 만들기
        I[i] /= diagon                                  #I에도 똑같은 연산
        #diagonal element 제외한 모든 성분 0으로 만들기(0부터 (n-1)th row까지 1씩 증가하며 반복)
        for k in range(n):
            if(k==i or A[k,i]==0): continue             #diagonal element이거나 각 성분이 0인 경우 건너뛰기(다음 k값으로 재실행)
            coeff = A[k,i]                              #각 성분들을 변수로 저장
            for m in range(i,n):                        #모든 m에 대해 A[k,m]에 "A[k,m]-A[k,i]*A[i,m]" 저장(k,i are fixed in each iteration)
                A[k,m] -= coeff*A[i,m]                  #★중요한 수식: i가 1씩 증가함에 따라 diagonal성분 제외한 모든 성분 0으로 만드는 수식★
            I[k] -= coeff*I[i]                          #I Matrix에도 마찬가지로 k의 증가에 따라 동일 연산
    return A, I                                         #새로운 A와 I 값 반환

A = [[10,9,8,4,1,0],[9,10,8,5,2,1],[8,8,10,7,4,2],[4,5,7,10,6,3],[1,2,4,6,10,5],[0,1,2,3,5,10]]                           #A matrix 입력(n*n Matrix)
I = [10,9,8,7,6,5]                           #I matrix 입력(n*n Matrix)

Tr_A,Tr_I = G_J_M_I(A,I)                                #G_J_M_I 함수 호출(argument: 입력받은 A, I), 반환 값을 Tr_A, Tr_I 변수에 저장
#출력문
print("A changes to Identity Matrix:")
print(Tr_A)
print("I changes to B(inverse of A): ")
print(Tr_I)
