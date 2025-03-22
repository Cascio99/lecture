/* 태양빛 도달 시간 계산*/
#include <stdio.h>

int main(void)
{
	double light_speed = 300000, distance = 149600000; /* 세 개의 변수 선언, 초기화*/
	int time, minute, second;

	time = distance / light_speed; /* 걸린 시간 = 이동 거리 / 빛의 속도*/
	minute = time / 60; /*분 = 걸린 시간 / 60*/
	second = time % 60; /*초 = 걸린 시간(초)을 60으로 나눈 값(분)에서 나머지 값*/

	printf("빛의 속도는 %lfkm/s \n", light_speed);
	printf("태양과 지구와의 거리 %lfkm \n", distance);
	printf("도달 시간은 %d분 %d초\n", minute, second);

	return 0;
}