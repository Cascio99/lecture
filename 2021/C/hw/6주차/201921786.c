#include <stdio.h>

int main(void)
{
	int a, b, c;

	printf("정수를 입력하시오:");
	scanf("%d", &a);
	printf("정수를 입력하시오:");
	scanf("%d", &b);

	c = a % b;

	switch (c)
	{
	case 0:
		printf("약수입니다.");
		break;
	default:
		printf("약수가 아닙니다.");
		break;
	}

	return 0;
}