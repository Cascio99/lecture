/*섭씨온도를 화씨온도로 환산하기*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	double C, F; /*변수 선언*/

	printf("섭씨값을 입력하시오:"); /*입력 안내메시지 출력*/
	scanf("%lf", &C); /*섭씨 온도 입력*/

	F = 9 * C / 5 + 32; /*관계식*/

	printf("화씨값은 %lf도입니다.", F); /*계산 결과 출력*/

	return 0;
}