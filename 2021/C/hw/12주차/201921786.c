/*2���� ������ �ִ������� �ּҰ���� ���ϱ�*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void get_lcm_gcd(int x, int y, int* p_lcm, int* p_gcd) {/*�ּҰ����(lcm)�� �ִ�����(gcd) ���ϴ� �Լ� ����*/
	int temp_x = x, temp_y = y;							/*���� x�� y�� ������ ���� ����*/
	
	while (y != 0) {									/*���� 276������ ����(��Ŭ������ �ִ����� ã�� �˰���)*/
		int r = x % y;
		x = y;
		y = r;
	}
	*p_gcd = x;											/*������ p_gcd�� ����Ű�� ������ ��: x�� ����� ��*/
	*p_lcm = (temp_x * temp_y) / *p_gcd;				/*�ּҰ���� ���ϴ� �˰���*/
	printf("�ּҰ������ %d�Դϴ�.\n", *p_lcm);
	printf("�ִ������� %d�Դϴ�.\n", *p_gcd);
}

int main()
{
	int a[2],l[1],g[1];									/*�� ��, �� ���� �ִ�����, �� ���� �ּҰ���� ���� �迭 ����*/
	printf("�� ���� ������ �Է��Ͻÿ�: ");
	scanf("%d %d", &a[0], &a[1]);						/*�� �� �Է�*/
	get_lcm_gcd(a[0], a[1],l,g);						/*�Լ� ȣ��*/
}