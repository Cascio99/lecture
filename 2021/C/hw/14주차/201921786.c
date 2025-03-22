#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	FILE* fp = NULL;											/*포인터 fp 선언*/
	fp = fopen("201921786.txt", "w");							/*파일 생성(쓰기 모드)*/
	int cur_col = 0;

	if (fp == NULL) printf("파일 출력 실패\n");
	else printf("파일 출력중...\n파일 출력 완료...\n");
	
	for (int a = 2; a < 6; a++) {								/*2단 ~ 5단임을 출력*/
		fprintf(fp, "\t%4d단\t", a);
		if (a == 5) {
			fprintf(fp, "\n");
			break;
		}
	}
	for (int i = 0; i < 2; i++) {								/*구구단 계산 결과 출력*/
		int j = 4 * i + 2;
		if (i == 1) {
			for (int a = 6; a < 10; a++) {
				fprintf(fp, "\t%4d단\t", a);
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
	fclose(fp);													/*파일 닫기*/
	return 0;
}