/*ASCII Code���� 16������ ��ȯ�ϴ� ���α׷�*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	char ch;													/*����(������) ����*/

	printf("���� �Է� : ");										/*�Է� �ȳ� ���� ���*/
	scanf("%c", &ch);											/*���� �� �Է�*/

	if (ch >= 'A' && ch <= 'Z') {								/*���� �빮���� ���*/
		printf("\n�Է¹��� : %c, ASCII CODE : %#x", ch, ch);	/*�Է� ���� �״�� ���, ASCII Code�� ���(16����), p.139 �������*/
		ch += 32;												/*�빮�ڡ�ҹ��� ��ȯ*/
		printf("\n��ȯ���� : %c, ASCII Code : %#x\n", ch, ch);	/*�ҹ��� ���, ASCII Code ���*/
	}
	else if (ch >= 'a' && ch <= 'z') {							/*���� �ҹ����� ���*/
		printf("\n�Է¹��� : %c, ASCII Code : %#x", ch, ch);	
		ch -= 32;
		printf("\n��ȯ���� : %c, ASCII Code : %#x\n", ch, ch);
	}
	else if (ch >= '0' && ch <= '9') {							/*������ ���*/
		printf("\n�Է¹��� : %c, ASCII Code : %#x", ch, ch);	/*�Է°� �״�� ���, ASCII Code�� �����ϴ� �� 16������ ���*/
		printf("\n��ȯ �� �� �����ϴ�.\n");						/*���ڿ��� ��/�ҹ��� ���� ���� ǥ��*/
	}
	else {														/*�Է°��� ����, ���ڰ� �ƴ� ���*/
		printf("\n�Է¹��� : %c, ASCII Code : %#x", ch, ch);	/*�״�� ���, ASCII Code ������ 16������ ���*/
		printf("\n��ȯ �� �� �����ϴ�.\n");
	}

	return 0;
}