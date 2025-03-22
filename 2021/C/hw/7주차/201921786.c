/*정수의 자리수 반대로 출력하기*/
#include <stdio.h>

int main(void)
{
	int n, r;							/*변수 선언*/

	printf("정수를 입력하시오: ");
	scanf("%d", &n);					

	do {
		r = n % 10;						/*10으로 나눴을 때 나머지*/
		printf("%d", r);				/*나머지 값 출력*/
		n = n / 10;						/*입력한 정수를 10으로 나눈 값*/
	} while (n > 0);					/*n값이 0이 나오면 반복 종료*/

	return 0;
}