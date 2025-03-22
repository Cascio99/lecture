/*정수의 자리수의 개수와 합 구하기*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int digit_num(int n);							/*자리수의 개수 구하는 함수 원형*/
int digit_sum(int n);							/*자리수의 합 구하는 함수 원형*/

int main(void)
{
	int z, x, y;								/*z: 입력할 정수, x: 자리수의 개수, y: 자리수의 합*/
	printf("정수를 입력하시오: ");
	scanf("%d", &z);
	y = z;										/*반복문 안에서 z값 변경되므로 미리 자리수의 합 구할 때 쓸 변수(y) 선언*/
	while (1) {									/*무한 반복문*/
		x = digit_num(z);						/*자리수 구하는 함수 호출 후 반환 값을 x에 저장*/
		if (z < 10) {							/*10보다 작으면 한 번만 시행 후 반복 종료*/
			printf("자리수의 개수: %d\n", x);
			break;
		}
		else z /= 10;							/*10보다 크면 10보다 작아질 때까지 10으로 나누기(정수)*/
	}
	printf("자리수의 합: %d", digit_sum(y));	/*자리수의 합 구하는 함수의 반환값 출력*/
	return 0;
}
int digit_num(int n) {							/*자리수의 개수 구하는 함수*/
	static int num = 1;							/*main함수 내의 반복문에서 반복하더라도 초기화되지 않도록 num을 정적 지역 변수로 설정*/
	if (n > 9) num++;							/*n이 9보다 크면 자리수를 1씩 증가*/
	return num;									/*자리수를 의미하는 num을 반환*/
}
int digit_sum(int n) {							/*자리수의 합 구하는 함수*/
	if (n < 10) return n;						/*n이 10보다 작으면 n을 그대로 반환*/
	else return (digit_sum(n / 10) + (n % 10));	/*n이 10보다 작을 때까지 n을 n/10으로 바꿔 함수 순환, 반환값은 역순으로 계산*/
}