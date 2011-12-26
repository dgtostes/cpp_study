#include <stdio.h>
#define PI 3.14


float circle_area(float radius)
{
	return PI*radius*radius;
}


main()
{
	float radius;
	printf("input the radius circle --> ");
	scanf("%f", &radius);
	printf("the circle area is --> %.2f u2\n\n", circle_area(radius));
}
