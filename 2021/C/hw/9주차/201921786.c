/*��Ģ���� ��� ���α׷�*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void intro();										/*�޴� �Լ� ���� ����*/
int add(int a, int b);								/*���� �Լ� ���� ����*/
int sub(int a, int b);								/*���� �Լ� ���� ����*/
int mul(int a, int b);								/*���� �Լ� ���� ����*/
int div(int a, int b);								/*������ �Լ� ���� ����*/
int rem(int a, int b);								/*������ �Լ� ���� ����*/

int main()
{
	int choice1, x, y, result = 0;					/*choice1:�޴�����, x: ù��° �ǿ�����, y;�ι�° �ǿ�����, result: ���*/
	char exit;										/*�������� ������� �����ϱ� ���� �ʿ��� ������ ����*/
	intro();										/*�ȳ��� �Լ� ȣ��*/
	while (1) {										/*���� �ݺ���*/
		printf("���ϴ� �޴��� �����Ͻÿ�(1-5): ");	
		scanf("%d", &choice1);
		printf("���� 2���� �Է��Ͻÿ�: ");
		scanf("%d %d", &x, &y);
		if (choice1 == 1) result = add(x, y);		/*���� ���� �� ���� �Լ� ȣ�� �� ��ȯ���� result ������ ����*/
		else if (choice1 == 2) result = sub(x, y);	/*�E�� ���� �� ���� �Լ� ȣ�� �� ��ȯ���� result ������ ����*/
		else if (choice1 == 3) result = mul(x, y);	/*���� ���� �� ���� �Լ� ȣ�� �� ��ȯ���� result ������ ����*/
		else if (choice1 == 4) result = div(x, y);	/*������ ���� �� ���� �Լ� ȣ�� �� ��ȯ���� result ������ ����*/
		else if (choice1 == 5) result = rem(x, y);	/*������ ���� �� ���� �Լ� ȣ�� �� ��ȯ���� result ������ ����*/
		else continue;							 	/*�Է� ������ �ݺ��� �����*/
		printf("������ :%d\n", result);			/*�������� ���*/

		printf("����Ϸ��� y�� �����ÿ�: ");		/*�������� ������� ���� �ȳ��� ���*/
		getchar();									/*���� scanf()���� ���� ����Ű ���ڸ� �����ϱ� ���� �ʿ�*/
		scanf("%c", &exit);							/*���� exit�� �� �Է¹ޱ�*/
		if (exit == 'y') continue;					/*'y'�̸� �ݺ��� �����*/
		else break;									/*'y'�� �ƴϸ� �ݺ��� ����*/
	}												/*"return;","return 0;"�� ���ų� �ƹ��͵� �� ������ ��ȯ���� �ʰ� ����*/
}

void intro()										/*��ȯ���� �����Ƿ� ��ȯ��:void, �Լ� �̸�:intro, �Ű����� �����Ƿ� ��ȣ �� ����*/
{													/*function body*/
	for (int i = 0; i < 40; i++) printf("=");		/*���� ���� �ݺ���*/
	printf("\n");
	printf("MENU\n");
	for (int i = 0; i < 40; i++) printf("=");
	printf("\n");
	printf("1. ����\n");							/*�޴� ���� �ȳ��� ���*/
	printf("2. ����\n");
	printf("3. ����\n");
	printf("4. ������\n");
	printf("5. ������\n");
}
int add(int a, int b)								/*��ȯ��:����, �Լ���:add, �Ű�����:���� a,b*/
{
	return(a + b);									/*���� ���� ������� ��ȯ*/
}
int sub(int a, int b)								/*��ȯ��:����, �Լ���sub, �Ű�����:���� a,b*/
{
	return(a - b);									/*���� ���� ������� ��ȯ*/
}
int mul(int a, int b)								/*��ȯ��:����, �Լ���mul, �Ű�����:���� a,b*/
{
	return(a * b);									/*���� ���� ������� ��ȯ*/
}
int div(int a, int b)								/*��ȯ��:����, �Լ���div, �Ű�����:���� a,b*/
{
	return(a / b);									/*������ ���� ������� ��ȯ*/
}
int rem(int a, int b)								/*��ȯ��:����, �Լ���rem, �Ű�����:���� a,b*/
{
	return(a % b);									/*������ ���� ������� ��ȯ*/
}