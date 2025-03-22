/*2개의 정수의 최대공약수와 최소공배수 구하기*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void get_lcm_gcd(int x, int y, int* p_lcm, int* p_gcd) {/*최소공배수(lcm)와 최대공약수(gcd) 구하는 함수 선언*/
	int temp_x = x, temp_y = y;							/*원래 x와 y값 저장할 변수 선언*/
	
	while (y != 0) {									/*교재 276페이지 참고(유클리드의 최대공약수 찾는 알고리즘)*/
		int r = x % y;
		x = y;
		y = r;
	}
	*p_gcd = x;											/*포인터 p_gcd가 가리키는 변수의 값: x에 저장된 값*/
	*p_lcm = (temp_x * temp_y) / *p_gcd;				/*최소공배수 구하는 알고리즘*/
	printf("최소공배수는 %d입니다.\n", *p_lcm);
	printf("최대공약수는 %d입니다.\n", *p_gcd);
}

int main()
{
	int a[2],l[1],g[1];									/*두 수, 두 수의 최대공약수, 두 수의 최소공배수 넣을 배열 선언*/
	printf("두 개의 정수를 입력하시오: ");
	scanf("%d %d", &a[0], &a[1]);						/*두 수 입력*/
	get_lcm_gcd(a[0], a[1],l,g);						/*함수 호출*/
}