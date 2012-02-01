#include <stdio.h>

float square_area(float side)
{
	return side*side;
}


main()
{
	float side;
	printf("input the square side --> ");
	scanf("%f", &side);
	printf("saquare area --> %.2f u2\ndouble square area --> %.2f u2\n\n", 
              square_area(side), 2*square_area(side));
}
