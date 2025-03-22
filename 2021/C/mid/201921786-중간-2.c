/*n 이하의 소수와 소수의 개수 찾기*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

/*소수: 1과 자기 자신만이 약수인 수*/

int main(void)
{
	int n, tempt = 0, p_num = 1;									/*n:입력값, tempt:시도 수, p_num: n이하의 소수의 개수(뒤에서 '2'가 생략되므로 1로 초기화)*/

	for (int t = 0; t < 3; t++) {									/*3번의 기회, n이 2이상이면 종료*/
		printf("입력한 정수까지 소수를 구합니다.\n");
		printf("정수를 입력해 주세요(2이상) : ");					/*입력안내메시지 출력*/
		scanf("%d", &n);											/*n 입력*/

		if (n > 1) {												/*2이상일 경우*/
			printf("\n%d 이하의 소수\n\n", n);
			printf("      2");										/*뒤의 반복문에서 2는 제외되기 떄문에 미리 2 출력*/
			for (int i = 2; i <= n; i++) {							/*i: 2부터 n까지 1씩 증가하며 소수 찾는 반복문*/
				for (int j = 2; j < i; j++) {						/*j: i를 나누는 값이고, i보다 1작은 값까지 1씩 증가*/
					if (i % j == 0)									/*나눠 떨어지면 약수가 "1,자기 자신" 제외 더 있기 때문에 다음 i 검사*/
						break;
					else if (i % j != 0 && j < i - 1)				/*j가 i-1보다 작으면서 나눠 떨어지지 않으면 다음 j 검사*/
						continue;
					else if (j == i - 1) {							/*위의 else if문을 반복하다가 j가 i-1이 되면 해당 i는 소수이므로 출력하고 다음 i 검사*/
						printf("%7d", i);							/*출력 필드의 폭: 7글자(교재 p.288)*/
						p_num++;									/*소수의 개수 count(1씩 증가)*/
						if (p_num % 10 == 0)						/*소수의 개수가 10개 출력될 때마다 줄 바꿈*/
							printf("\n");
						break;
					}
				}
			}
			printf("\n\n%d 이하의 소수는 %d개 입니다.\n", n, p_num);/*i를 n이 될 때까지 검사 완료시 count된 p_num(소수의 개수) 출력하고 종료*/
			break;
		}
		else {														/*2 미만인 값을 입력한 경우*/
			tempt++;												/*시도 횟수 1씩 증가*/
			printf("\n%d회 입력 오류입니다.\n\n", tempt);			/*시도 횟수(입력 오류 횟수) 출력*/
			continue;												/*n값 다시 입력하도록 바깥 반복문 재실행*/
		}
	}
	return 0;
}