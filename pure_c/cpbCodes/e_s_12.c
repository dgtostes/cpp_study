#include <stdio.h>

float ideal_weight(float height)
{
	return (72.7*height)-58;
}


main()
{
	float height;
	printf("input your height ---> ");
	scanf("%f", &height);
	printf("your Ideal weight is --> %.2f\n\n", ideal_weight(height));
}

