/*�����µ��� ȭ���µ��� ȯ���ϱ�*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	double C, F; /*���� ����*/

	printf("�������� �Է��Ͻÿ�:"); /*�Է� �ȳ��޽��� ���*/
	scanf("%lf", &C); /*���� �µ� �Է�*/

	F = 9 * C / 5 + 32; /*�����*/

	printf("ȭ������ %lf���Դϴ�.", F); /*��� ��� ���*/

	return 0;
}