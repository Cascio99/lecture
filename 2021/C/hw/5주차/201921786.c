/*cmŰ�� ��Ʈ�� ��ġ�� ��ȯ�ϱ�*/
#include <stdio.h>

int main(void)
{
	int input, feet;
	double remainder_cm, inch;
	const double INCH_PER_FEET = 12, CM_PER_INCH = 2.54;

	printf("Ű�� �Է��Ͻÿ�(cm): ");
	scanf("%d", &input);

	feet = input / (INCH_PER_FEET * CM_PER_INCH);
	remainder_cm = input - (feet * INCH_PER_FEET * CM_PER_INCH);
	inch = remainder_cm / CM_PER_INCH;

	printf("%dcm�� %d��Ʈ %lf��ġ�Դϴ�.\n", input, feet, inch);

	return 0;
}