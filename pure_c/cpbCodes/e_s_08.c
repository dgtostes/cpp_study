#include <stdio.h>

float salary_calc(float hour_money, float worked_hours)
{
	return hour_money*worked_hours;
}


main()
{
	float hour_money, worked_hours;
	printf("input your your hour value --> ");
	scanf("%f", &hour_money);
	printf("input the qty of worked hours --> ");
	scanf("%f", &worked_hours);
	printf("your salary is --> R$ %.2f\n\n", salary_calc(hour_money, worked_hours));
}
