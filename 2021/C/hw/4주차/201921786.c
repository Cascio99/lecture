/* �¾�� ���� �ð� ���*/
#include <stdio.h>

int main(void)
{
	double light_speed = 300000, distance = 149600000; /* �� ���� ���� ����, �ʱ�ȭ*/
	int time, minute, second;

	time = distance / light_speed; /* �ɸ� �ð� = �̵� �Ÿ� / ���� �ӵ�*/
	minute = time / 60; /*�� = �ɸ� �ð� / 60*/
	second = time % 60; /*�� = �ɸ� �ð�(��)�� 60���� ���� ��(��)���� ������ ��*/

	printf("���� �ӵ��� %lfkm/s \n", light_speed);
	printf("�¾�� �������� �Ÿ� %lfkm \n", distance);
	printf("���� �ð��� %d�� %d��\n", minute, second);

	return 0;
}