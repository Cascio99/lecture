#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE* fp = NULL;											/*������ fp ����*/
	fp = fopen("201921786.txt", "w");							/*���� ����(���� ���)*/
	int cur_col = 0;

	if (fp == NULL) printf("���� ��� ����\n");
	else printf("���� �����...\n���� ��� �Ϸ�...\n");
	
	for (int a = 2; a < 6; a++) {								/*2�� ~ 5������ ���*/
		fprintf(fp, "\t%4d��\t", a);
		if (a == 5) {
			fprintf(fp, "\n");
			break;
		}
	}
	for (int i = 0; i < 2; i++) {								/*������ ��� ��� ���*/
		int j = 4 * i + 2;
		if (i == 1) {
			for (int a = 6; a < 10; a++) {
				fprintf(fp, "\t%4d��\t", a);
				if (a == 9) {
					fprintf(fp, "\n");
					break;
				}
			}
		}
		for (int n = 1; n < 10; n++) {
			for (int m = j; m < j + 4; m++) {
				fprintf(fp, "%13d x %d = %2d\t", m, n, m * n);
				cur_col++;
				if (cur_col % 4 == 0) fprintf(fp, "\n");
			}
			if (n == 9) break;
		}
	}
	fclose(fp);													/*���� �ݱ�*/
	return 0;
}