/*알파벳 개수 알아내기*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char arr[26] = { 0 }, str[100];					/*arr:각각의 알파벳 개수 저장하는 배열(모두 0으로 초기화), str:입력받을 문자 저장할 배열*/
	printf("문자열 입력: ");
	scanf("%[^\n]s", &str);							/*엔터를 제외한 모든 문자열을 받기*/
	for (int j = 0; j < 100; j++) {
		if ('a' <= str[j] && str[j] <= 'z') {		/*각 인덱스에 저장된 데이터가 소문자인 경우*/
			int x = str[j] - 'a';					/*x:str의 각 인덱스에 저장된 아스키 코드 - 'a', x는 0부터 25까지*/
			arr[x]++;								/*각각의 알파벳을 포함하므로 각각의 arr[x] 1씩 증가*/
		}
		else if ('A' <= str[j] && str[j] <= 'Z') {	/*각 인덱스에 저장된 데이터가 대문자인 경우*/
			int X = str[j] - 'A';					/*Z:str의 각 인덱스에 저장된 아스키 코드 - 'A', X는 0부터 25까지*/
			arr[X]++;								/*각각의 알파벳을 포함하므로 각각의 arr[X]를 1씩 증가*/
		}
	}
	char a_to_z[26];								/*알파벳 저장할 배열 선언*/
	for (int i = 97; i < 123; i++) {				/*a의 아스키 코드:97, z의 아스키 코드: 122*/
		a_to_z[i-97] = i;							/*a_to_z 배열의 인덱스 0부터 알파벳 저장*/
		printf("%3c", a_to_z[i-97]);				/*3칸 간격으로 출력*/
	}
	printf("\n");
	for (int k = 0; k < 26; k++)					/*3칸 간격으로 각각의 알파벳 개수 저장된 arr[] 배열 출력*/
		printf("%3d", arr[k]);
}