#include <stdio.h>

float soma(float a, float b)
{
	return a+b;
}

main()
{
	float a, b;
	printf("input a number --> ");
	scanf("%f", &a);
	printf("input another number --> ");
	scanf("%f", &b);
	printf("The %.2f + %.2f is --> %.2f\n", a,b, soma(a,b));
}
