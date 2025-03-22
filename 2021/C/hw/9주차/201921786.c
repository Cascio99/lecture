/*사칙연산 계산 프로그램*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
void intro();										/*메뉴 함수 원형 정의*/
int add(int a, int b);								/*덧셈 함수 원형 정의*/
int sub(int a, int b);								/*뺄셈 함수 원형 정의*/
int mul(int a, int b);								/*곱셈 함수 원형 정의*/
int div(int a, int b);								/*나눗셈 함수 원형 정의*/
int rem(int a, int b);								/*나머지 함수 원형 정의*/

int main()
{
	int choice1, x, y, result = 0;					/*choice1:메뉴선택, x: 첫번째 피연산자, y;두번째 피연산자, result: 결과*/
	char exit;										/*종료할지 계속할지 선택하기 위해 필요한 문자형 변수*/
	intro();										/*안내문 함수 호출*/
	while (1) {										/*무한 반복문*/
		printf("원하는 메뉴를 선택하시오(1-5): ");	
		scanf("%d", &choice1);
		printf("숫자 2개를 입력하시오: ");
		scanf("%d %d", &x, &y);
		if (choice1 == 1) result = add(x, y);		/*덧셈 선택 시 덧셈 함수 호출 후 반환값을 result 변수에 저장*/
		else if (choice1 == 2) result = sub(x, y);	/*뺼셈 선택 시 덧셈 함수 호출 후 반환값을 result 변수에 저장*/
		else if (choice1 == 3) result = mul(x, y);	/*곱셈 선택 시 덧셈 함수 호출 후 반환값을 result 변수에 저장*/
		else if (choice1 == 4) result = div(x, y);	/*나눗셈 선택 시 덧셈 함수 호출 후 반환값을 result 변수에 저장*/
		else if (choice1 == 5) result = rem(x, y);	/*나머지 선택 시 덧셈 함수 호출 후 반환값을 result 변수에 저장*/
		else continue;							 	/*입력 오류시 반복문 재실행*/
		printf("연산결과 :%d\n", result);			/*연산결과값 출력*/

		printf("계속하려면 y를 누르시오: ");		/*종료할지 계속할지 묻는 안내문 출력*/
		getchar();									/*위의 scanf()에서 누른 엔터키 문자를 삭제하기 위해 필요*/
		scanf("%c", &exit);							/*변수 exit의 값 입력받기*/
		if (exit == 'y') continue;					/*'y'이면 반복문 재실행*/
		else break;									/*'y'가 아니면 반복문 종료*/
	}												/*"return;","return 0;"를 쓰거나 아무것도 안 적으면 반환하지 않고 종료*/
}

void intro()										/*반환값이 없으므로 반환형:void, 함수 이름:intro, 매개변수 없으므로 괄호 안 공백*/
{													/*function body*/
	for (int i = 0; i < 40; i++) printf("=");		/*밑줄 생성 반복문*/
	printf("\n");
	printf("MENU\n");
	for (int i = 0; i < 40; i++) printf("=");
	printf("\n");
	printf("1. 덧셈\n");							/*메뉴 선택 안내문 출력*/
	printf("2. 뺄셈\n");
	printf("3. 곱셈\n");
	printf("4. 나눗셈\n");
	printf("5. 나머지\n");
}
int add(int a, int b)								/*반환형:정수, 함수명:add, 매개변수:정수 a,b*/
{
	return(a + b);									/*덧셈 수식 결과값을 반환*/
}
int sub(int a, int b)								/*반환형:정수, 함수명sub, 매개변수:정수 a,b*/
{
	return(a - b);									/*뺄셈 수식 결과값을 반환*/
}
int mul(int a, int b)								/*반환형:정수, 함수명mul, 매개변수:정수 a,b*/
{
	return(a * b);									/*곱셈 수식 결과값을 반환*/
}
int div(int a, int b)								/*반환형:정수, 함수명div, 매개변수:정수 a,b*/
{
	return(a / b);									/*나눗셈 수식 결과값을 반환*/
}
int rem(int a, int b)								/*반환형:정수, 함수명rem, 매개변수:정수 a,b*/
{
	return(a % b);									/*나머지 수식 결과값을 반환*/
}