/*cm키를 피트와 인치로 변환하기*/
#include <stdio.h>

int main(void)
{
	int input, feet;
	double remainder_cm, inch;
	const double INCH_PER_FEET = 12, CM_PER_INCH = 2.54;

	printf("키를 입력하시오(cm): ");
	scanf("%d", &input);

	feet = input / (INCH_PER_FEET * CM_PER_INCH);
	remainder_cm = input - (feet * INCH_PER_FEET * CM_PER_INCH);
	inch = remainder_cm / CM_PER_INCH;

	printf("%dcm는 %d피트 %lf인치입니다.\n", input, feet, inch);

	return 0;
}