#include <stdio.h>

int main(void)
{
	int a, b, c;

	printf("������ �Է��Ͻÿ�:");
	scanf("%d", &a);
	printf("������ �Է��Ͻÿ�:");
	scanf("%d", &b);

	c = a % b;

	switch (c)
	{
	case 0:
		printf("����Դϴ�.");
		break;
	default:
		printf("����� �ƴմϴ�.");
		break;
	}

	return 0;
}