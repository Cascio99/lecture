/*���Ǳ� ���α׷�*/
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
double m_BMR(double W, double H, int Y);
double f_BMR(double W, double H, int Y);
void menu();
/*������ ������ ���ʴ�緮 ���ϴ� �Լ�, �޴� �����ִ� �Լ� ����*/
struct desserts {
	char name[20];
	int price;
	int stock;
	int calories;
};
/*�Ľ��� �±׷� ���� �̸�, ����, ���, Į�θ��� ����� �ϴ� ����ü ����*/
struct desserts list[] = { {"Jelly",1000,100,95},
	{"Milk tea",3500,100,45},
	{"Gum",500,100,10},
	{"Coffee",5000,50,135},
	{"Coke",3000,60,92},
	{"Ice cream",4000,55,267},
	{"Sprite",3000,60,96},
	{"Pepsi",3000,60,90} };
/*��ǰ ����Ʈ�� ����ü �迭�� ����*/
int main(void)
{
	char s, buy_more;
	double w, h;
	int y;
	int input_money,total_calories = 0, total_price = 0;
	int choice;
	/*���� ������ �̸� ����*/
	menu();
	/*�޴� �Լ� ȣ��*/
	FILE* fp = NULL;
	fp = fopen("���Ǳ� ���.txt", "w");
	/*������� ���� ����*/
	printf("\n���� �� �� ���� �Ľ��� �ԱⰡ �η���Ű���?\n");
	printf("�� ���Ǳ�� ����� ���ʴ�緮�� Ȱ����緮�� �˷��ְ� �ֽ��ϴ�!\n");
	printf("����, ü��, Ű, ���̸� �Է��Ͻø� �˴ϴ�!\n");
	while (1) {
		printf("����(����: m, ����: f): ");
		scanf("%s", &s);
		getchar();								/*���� scanf()���� ���� ����Ű ���ڸ� �����ϱ� ���� �ʿ�*/
		printf("ü��(kg): ");
		scanf("%lf", &w);
		printf("Ű(cm): ");
		scanf("%lf", &h);
		printf("����(��): ");
		scanf("%d", &y);
		if (s == 'm' || s == 'M') {
			double value = m_BMR(w, h, y);
			printf("����� ���ʴ�緮�� %lfkcal�̰�, Ȱ����緮�� %lfKcal�Դϴ�.(�� 1~3�� � ����)\n", value, 0.375 * value);
			break;
		}
		else if (s == 'f' || s == 'F') {
			double value = f_BMR(w, h, y);
			printf("����� ���ʴ�緮�� %lfkcal�̰�, Ȱ����緮�� %lfKcal�Դϴ�.(�� 1~3�� � ����)\n", value, 0.375 * value);
			break;
		}
		/*�� ������ ���� ����,Ȱ����緮 �ȳ��� ���*/
		else {
			printf("�ءؼ����� ���Է����ֽʽÿ��ء�\n");
			continue;
		}
	}
	/*����,Ȱ����緮 �ȳ��� ��� �� ���� ���� �ȳ�*/
	while (1) {
		printf("���Ա��� 500�� �̻��� ���� �־��ֽʽÿ�(�����ڸ� ���� �ݾ� ���� ����): ");
		scanf("%d", &input_money);
		if ((input_money % 10) != 0 || input_money < 500) {
			printf("�ءشٽ� �־��ֽʽÿ��ء�\n");
			continue;
		}
		else break;
	}
	/*temp_money: ó���� ���� �ݾ�, input_money: ���� ��ǰ ��鼭 ���� �Ǵ� �ݾ�*/
	int temp_money = input_money;
	/*�ء��߿��� ���ѹݺ����� ����: ���� ���šء�*/
	while (1) {
		menu();
		printf("��ǰ��ȣ�� �Է��Ͻʽÿ�(1~8): ");
		scanf("%d", &choice);
		/*�޴� ��ȳ� �� ��ǰ��ȣ(1~8) �Է� �ȳ���*/
		if (choice > 0 && choice < 9) {
			if (input_money < list[choice - 1].price) {
				/*�ܾ��� ������ ������ �ݾ׺��� ���� ���*/
				if (input_money < 500) {
					/*���� �� ������ ��(500��)�̹Ƿ� �ܾ��� 500�� �̸��̸� ����*/
					printf("�ءش� �̻� �� �� �ִ� ��ǰ�� �����ϴ١ء�");
					break;
				}
				/*�ܾ��� 500�� �̻������� ������ ������ �� �� ����*/
				printf("�ء��� ��ǰ�� ��⿡�� ���� �����ϴ١ء�");
				continue;
			}
			else {
				/*���������� ������ ������ �� �ִ� ���*/
				total_price += list[choice - 1].price;
				total_calories += list[choice - 1].calories;
				input_money -= list[choice - 1].price;
				list[choice - 1].stock--;
				/*total_price: �� ���ұݾ�, total_calories: �� ���� Į�θ�, input_money: �ܾ�, list[choice-1].stock: ���Ǳ� �� ������ ������ ��� �� ����*/
				printf("�� ������ ������ �ֽ��ϱ�? Y(��): ");
				scanf("%s", &buy_more);
				getchar();					/*���� scanf()���� ���� ����Ű ���ڸ� �����ϱ� ���� �ʿ�*/
				if (buy_more == 'y' || buy_more == 'Y') continue;
				else break;
				/*y�� Y�� ������ �� �����ϵ���, �ƴϸ� �����ϵ��� ����*/
			}
		}
		else continue;
	}
	/*�Ž����� ����*/
	int change = temp_money - total_price;
	int change_5000 = change / 5000;
	int change_1000 = (change % 5000) / 1000;
	int change_500 = (change % 1000) / 500;
	int change_100 = (change % 500) / 100;
	int change_50 = (change % 100) / 50;
	int change_10 = (change % 50) / 10;
	printf("\n�Ž����� %d���� �������ʽÿ�\n5000����: %d / 1000����: %d / 500��¥�� ����: %d / 100��¥�� ����: %d / 50��¥�� ����: %d / 10��¥�� ����: %d\n", change, change_5000, change_1000, change_500, change_100, change_50, change_10);
	/*�����ϰ� �� Į�θ� �ȳ�*/
	printf("���ϲ��� ������ ��ǰ�� �� Į�θ��� %dkcal�Դϴ�.\n", total_calories);
	/*"���Ǳ� ���.txt"���Ͽ��� �� ��ǰ�� ��� �� ���*/
	for (int i = 0; i < 8; i++) fprintf(fp, "%s�� ���� %d�� ���ҽ��ϴ�.\n", list[i].name, list[i].stock);
	/*���� �ݱ�*/
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
		printf("%d��: %s %d�� %dkcal\n", a + 1, list[a].name, list[a].price, list[a].calories);
	}
}