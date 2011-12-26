#include <stdio.h>

float f2c(float f_temp)
{
	return (5*(f_temp-32)/9);
}

main()
{
	float temp_f;
	printf("input a farenheit temp --> ");
	scanf("%f", &temp_f);
	printf("%.2f F ---> %f C\n\n", temp_f, f2c(temp_f));
}


