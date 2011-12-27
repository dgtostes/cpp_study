#include <stdio.h>

float over_weight(float weight)
{
	return weight - 50;
}

float tax_calculator(float over_weight)
{
	return over_weight*4.0;
}

main()
{	
	float weight;
	float o_weight;
	printf("input the fish weight --> ");
	scanf("%f", &weight);
	o_weight = over_weight(weight);
	if(o_weight > 0)
	{
		printf("you have a over weight of %.2f kg\nTax: $ %.2f\n\n", o_weight, tax_calculator(o_weight));
	}
	else
	{
		printf("no over weight\n\n");
	}
}
