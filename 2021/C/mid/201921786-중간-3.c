/*1~99 사이의 구구단 출력*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int dan_i, dan_f, col_input, column_1 = 0, column_2 = 0;							/*column_1, column_2: 현재 출력한 열수, 0으로 초기화*/
	printf("시작 단을 입력하세요(1~99) : ");
	scanf("%d", &dan_i);
	printf("종료 단을 입력하세요(1~99) : ");
	scanf("%d", &dan_f);
	printf("출력할 열 수를 입력하세요(1~7) : ");
	scanf("%d", &col_input);

	if (dan_i < 1 || dan_i > 99 || dan_f < 1 || dan_f > 99) {							/*시작 단과 종료 단이 둘 중 하나라도 범위 밖이면 오류메시지 출력 후 종료(논리 연산자 OR)*/
		printf("단수 입력 범위 오류입니다.\n");
		return 0;
	}
	else if (col_input < 1 || col_input > 7) {											/*열수가 범위 밖이면 오류메시지 출력 후 종료*/
		printf("출력 열수 입력 범위 오류입니다.\n");
		return 0;
	}
	else if (dan_i > dan_f) {															/*종료 단보다 시작 단이 크면 오류메시지 출력 후 종료(관계 연산자 사용)*/
		printf("종료 단보다 시작 단이 큰 오류입니다.\n");
		return 0;
	}
	else {																				/*범위 조건 모두 만족하면 시작 단부터 종료 단까지 구구단 출력열수로 출력 후 종료*/
		for (int i = dan_i; i <= dan_f; i++) {											/*시작 단부터 종료 단까지 반복*/
			for (int j = 1; j <= col_input; j++) {										/*출력열수 제어*/
				if (((dan_i - 1) + col_input) > dan_f) {								/*★마지막 행일 경우 조건 제어(종료 단까지만 출력해야 하기 때문에)*/
					col_input = (dan_f - (dan_i - 1)) % col_input;						/*출력할 열수 재선언*/
					for (int m = dan_i; m <= dan_f; m++) {								/*재선언된 마지막 행의 시작 단부터 종료 단까지 출력 반복*/
						for (int n = 1; n <= col_input; n++) {							/*위에서 재선언된 출력할 열수까지 출력 반복*/
							printf("%6d 단       ", m);									/*출력필드 폭{6글자(교재 p.288)}으로 몇 단을 계산 중인지 출력*/
							m++;
							if (n == col_input) {										/*열수까지 '몇 단인지 알려주는 메시지'를 출력했으면 구구단 계산 값 출력 실행*/
								printf("\n");											/*알아보기 쉽게 줄바꿈*/
								for (int o = 1; o < 10; o++) {							/*9단까지 반복*/
									for (int p = dan_i; p < dan_i + col_input; p++) {	/*재선언된 시작 단부터 종료 단까지 출력*/
										printf("%2d x %2d = %3d   ", p, o, p * o);		/*계산 식 출력*/
										column_2++;										/*현재 출력한 열수 1씩 증가해서 변수 재선언(증감 연산자 사용)*/
										if (column_2 % col_input == 0)					/*현재 출력한 열수가 재선언된 출력 열수가 되면 줄바꿈*/
											printf("\n");
									}
									if (o == 9) {										/*9단까지 출력하면 가장 가까운 바깥 반복문 종료*/
										m--;											/*앞에서m을 1 더했으므로 다시 1 빼기*/
										break;
									}
								}
							}


						}
					}
					return 0;															/*9단까지 다 출력했으면 실행 종료*/
				}
				printf("%6d 단       ", i);												/*몇 단 계산하는지 알려주는 메시지 출력*/
				i++;																	/*시작 단부터 종료 단까지 출력해야하므로 1씩 증가*/

				if (j == col_input) {													/*★마지막 행이 되기 전까지는 이 반복문 실행*/
					printf("\n");														/*구구단 계산 식 보기 쉽게 줄바꿈 특수 문자열 사용*/
					for (int k = 1; k < 10; k++) {										/*1단부터 9단까지 출력*/
						for (int l = dan_i; l < dan_i + col_input; l++) {				/*시작 단(입력된 열수까지 출력하면 재선언됨)부터 종료 단까지 출력*/
							printf("%2d x %2d = %3d   ", l, k, l * k);					/*식별하기 쉽게 필드 폭 조절*/
							column_1++;													/*현재 출력한 열수 1씩 증가해서 카운트*/
							if (column_1 % col_input == 0)								/*현재 출력한 열수가 입력된 열수이면 줄바꿈*/
								printf("\n");
						}
						if (k == 9) {													/*9단까지 출력하면 가장 가까운 바깥 반복문 종료*/
							i--;														/*위에서 i 1 더했으므로 다시 1 빼기*/
							dan_i += col_input;											/*시작 단 재설정 식*/
							break;
						}
					}
				}
			}
		}
	}
	return 0;
}