/*자판기 프로그램*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
double m_BMR(double W, double H, int Y);
double f_BMR(double W, double H, int Y);
void menu();
/*남성과 여성의 기초대사량 구하는 함수, 메뉴 보여주는 함수 선언*/
struct desserts {
	char name[20];
	int price;
	int stock;
	int calories;
};
/*후식을 태그로 갖고 이름, 가격, 재고, 칼로리를 멤버로 하는 구조체 선언*/
struct desserts list[] = { {"Jelly",1000,100,95},
	{"Milk tea",3500,100,45},
	{"Gum",500,100,10},
	{"Coffee",5000,50,135},
	{"Coke",3000,60,92},
	{"Ice cream",4000,55,267},
	{"Sprite",3000,60,96},
	{"Pepsi",3000,60,90} };
/*제품 리스트를 구조체 배열로 선언*/
int main(void)
{
	char s, buy_more;
	double w, h;
	int y;
	int input_money,total_calories = 0, total_price = 0;
	int choice;
	/*여러 변수들 미리 선언*/
	menu();
	/*메뉴 함수 호출*/
	FILE* fp = NULL;
	fp = fopen("자판기 재고.txt", "w");
	/*쓰기모드로 파일 열기*/
	printf("\n살이 찔 것 같아 후식을 먹기가 두려우신가요?\n");
	printf("이 자판기는 당신의 기초대사량과 활동대사량도 알려주고 있습니다!\n");
	printf("성별, 체중, 키, 나이만 입력하시면 됩니다!\n");
	while (1) {
		printf("성별(남성: m, 여성: f): ");
		scanf("%s", &s);
		getchar();								/*위의 scanf()에서 누른 엔터키 문자를 삭제하기 위해 필요*/
		printf("체중(kg): ");
		scanf("%lf", &w);
		printf("키(cm): ");
		scanf("%lf", &h);
		printf("나이(만): ");
		scanf("%d", &y);
		if (s == 'm' || s == 'M') {
			double value = m_BMR(w, h, y);
			printf("당신의 기초대사량은 %lfkcal이고, 활동대사량은 %lfKcal입니다.(주 1~3일 운동 기준)\n", value, 0.375 * value);
			break;
		}
		else if (s == 'f' || s == 'F') {
			double value = f_BMR(w, h, y);
			printf("당신의 기초대사량은 %lfkcal이고, 활동대사량은 %lfKcal입니다.(주 1~3일 운동 기준)\n", value, 0.375 * value);
			break;
		}
		/*각 성별에 따른 기초,활동대사량 안내문 출력*/
		else {
			printf("※※성별을 재입력해주십시오※※\n");
			continue;
		}
	}
	/*기초,활동대사량 안내문 출력 후 동전 투입 안내*/
	while (1) {
		printf("투입구에 500원 이상의 돈을 넣어주십시오(일의자리 수의 금액 투입 금지): ");
		scanf("%d", &input_money);
		if ((input_money % 10) != 0 || input_money < 500) {
			printf("※※다시 넣어주십시오※※\n");
			continue;
		}
		else break;
	}
	/*temp_money: 처음에 넣은 금액, input_money: 여러 제품 사면서 남게 되는 금액*/
	int temp_money = input_money;
	/*※※중요한 무한반복루프 시작: 간식 구매※※*/
	while (1) {
		menu();
		printf("제품번호를 입력하십시오(1~8): ");
		scanf("%d", &choice);
		/*메뉴 재안내 및 제품번호(1~8) 입력 안내문*/
		if (choice > 0 && choice < 9) {
			if (input_money < list[choice - 1].price) {
				/*잔액이 선택한 간식의 금액보다 작은 경우*/
				if (input_money < 500) {
					/*가장 싼 간식은 껌(500원)이므로 잔액이 500원 미만이면 종료*/
					printf("※※더 이상 살 수 있는 제품이 없습니다※※");
					break;
				}
				/*잔액이 500원 이상이지만 선택한 간식은 살 수 없음*/
				printf("※※이 제품을 사기에는 돈이 적습니다※※");
				continue;
			}
			else {
				/*정상적으로 간식을 구매할 수 있는 경우*/
				total_price += list[choice - 1].price;
				total_calories += list[choice - 1].calories;
				input_money -= list[choice - 1].price;
				list[choice - 1].stock--;
				/*total_price: 총 지불금액, total_calories: 총 섭취 칼로리, input_money: 잔액, list[choice-1].stock: 자판기 속 선택한 간식의 재고 수 선언*/
				printf("더 구매할 의향이 있습니까? Y(예): ");
				scanf("%s", &buy_more);
				getchar();					/*위의 scanf()에서 누른 엔터키 문자를 삭제하기 위해 필요*/
				if (buy_more == 'y' || buy_more == 'Y') continue;
				else break;
				/*y나 Y를 누르면 더 구매하도록, 아니면 종료하도록 설정*/
			}
		}
		else continue;
	}
	/*거스름돈 계산식*/
	int change = temp_money - total_price;
	int change_5000 = change / 5000;
	int change_1000 = (change % 5000) / 1000;
	int change_500 = (change % 1000) / 500;
	int change_100 = (change % 500) / 100;
	int change_50 = (change % 100) / 50;
	int change_10 = (change % 50) / 10;
	printf("\n거스름돈 %d원을 가져가십시오\n5000원권: %d / 1000원권: %d / 500원짜리 동전: %d / 100원짜리 동전: %d / 50원짜리 동전: %d / 10원짜리 동전: %d\n", change, change_5000, change_1000, change_500, change_100, change_50, change_10);
	/*섭취하게 될 칼로리 안내*/
	printf("귀하께서 구매한 제품의 총 칼로리는 %dkcal입니다.\n", total_calories);
	/*"자판기 재고.txt"파일에다 각 제품의 재고 수 출력*/
	for (int i = 0; i < 8; i++) fprintf(fp, "%s는 현재 %d개 남았습니다.\n", list[i].name, list[i].stock);
	/*파일 닫기*/
	fclose(fp);
	return 0;
}
double m_BMR(double W, double H, int Y) {
	return 66.47 + (13.75 * W) + (5 * H) - (6.76 * Y);
}
double f_BMR(double W, double H, int Y) {
	return 655.1 + (9.56 * W) + (1.85 * H) - (4.68 * Y);
}
void menu() {
	printf("\n===========MENU===========\n");
	for (int a = 0; a < 8; a++) {
		printf("%d번: %s %d원 %dkcal\n", a + 1, list[a].name, list[a].price, list[a].calories);
	}
}