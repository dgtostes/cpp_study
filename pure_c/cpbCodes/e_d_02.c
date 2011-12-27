#include <stdio.h>
#include "dgt_lib.h"

int is_negative(float number)
{
	if(number>=0)
	{
		printf("%f is positive\n\n", number);
		return 0;
	}
	else
	{
		printf("%f is negative\n\n", number);
		return 0;
	}
}

main()
{
	float number;
	number = ask4float("input a number --> ");
	is_negative(number);
}
