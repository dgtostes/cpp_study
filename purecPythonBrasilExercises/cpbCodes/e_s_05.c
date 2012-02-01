#include <stdio.h>

float m2c(float u)
{
	return u*100;
}

main()
{
	float unit;
	printf("input a value in m --> ");
	scanf("%f", &unit);
	printf("%.2f meter = %.2f cm\n\n", unit, m2c(unit));

}
