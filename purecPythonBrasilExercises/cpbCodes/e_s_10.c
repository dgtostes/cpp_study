#include <stdio.h>

float c2f(float c_temp)
{
	return (9/5*(c_temp)+32);
}


main()
{
	float temp_c;
	printf("input a celsius temp --> ");
	scanf("%f", &temp_c);
	printf("%.2f C ----> %.2f F\n\n", temp_c, c2f(temp_c));
}

