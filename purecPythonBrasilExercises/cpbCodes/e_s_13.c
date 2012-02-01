#include <stdio.h>

float ideal_weight(float height, int sex)
{
	if(sex == 1)
	{
		return (72.7*height) - 58; 
	}
	else{
		return (62.1*height) - 44.7;

	}
}


int compare(float ideal_w, float weight)
{
	if(ideal_w > weight)
	{
		printf("your are bellow than you ideal weight\n\n");
	}
	if(ideal_w < weight)
	{
                printf("your are over than you ideal weight\n\n");		
	}
	if(ideal_w == weight)
	{	
		printf("you are on your ideal weight\n\n");
	}

	return 0;
}


main()
{
	int sex;
	float height;
	float ideal_w, weight;
	printf("input your sex male(1) or female(2) --> ");
	scanf("%d", &sex);
	printf("input your height --> ");
        scanf("%f", &height);
	printf("input your weight --> ");
	scanf("%f", &weight);
	ideal_w = ideal_weight(height, sex);
	printf("your ideal weight is --> %.2f\n\n", ideal_w);
	compare(ideal_w,weight);
}

