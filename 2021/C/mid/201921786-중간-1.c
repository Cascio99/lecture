/*ASCII Code값을 16진수로 변환하는 프로그램*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	char ch;													/*변수(문자형) 선언*/

	printf("문자 입력 : ");										/*입력 안내 문자 출력*/
	scanf("%c", &ch);											/*변수 값 입력*/

	if (ch >= 'A' && ch <= 'Z') {								/*영어 대문자일 경우*/
		printf("\n입력문자 : %c, ASCII CODE : %#x", ch, ch);	/*입력 문자 그대로 출력, ASCII Code로 출력(16진수), p.139 참고사항*/
		ch += 32;												/*대문자→소문자 변환*/
		printf("\n변환문자 : %c, ASCII Code : %#x\n", ch, ch);	/*소문자 출력, ASCII Code 출력*/
	}
	else if (ch >= 'a' && ch <= 'z') {							/*영어 소문자일 경우*/
		printf("\n입력문자 : %c, ASCII Code : %#x", ch, ch);	
		ch -= 32;
		printf("\n변환문자 : %c, ASCII Code : %#x\n", ch, ch);
	}
	else if (ch >= '0' && ch <= '9') {							/*숫자일 경우*/
		printf("\n입력문자 : %c, ASCII Code : %#x", ch, ch);	/*입력값 그대로 출력, ASCII Code에 대응하는 값 16진수로 출력*/
		printf("\n변환 할 수 없습니다.\n");						/*숫자에는 대/소문자 구분 없음 표현*/
	}
	else {														/*입력값이 영어, 숫자가 아닌 경우*/
		printf("\n입력문자 : %c, ASCII Code : %#x", ch, ch);	/*그대로 출력, ASCII Code 대응값 16진수로 출력*/
		printf("\n변환 할 수 없습니다.\n");
	}

	return 0;
}