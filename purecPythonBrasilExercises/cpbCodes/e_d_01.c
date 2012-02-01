#include <stdio.h>
#include "dgt_lib.h"

float upper(float number1, float number2)
{
	if(number1>=number2)
	{
		return number1;	
	}
	else
	{
		return number2;
	}
}

	
main()
{	
	float number1, number2;
	number1 = ask4float("input a number --> ");
	number2 = ask4float("input other number --> ");
	printf("%f is the bigger number inputed\n\n", upper(number1, number2));
	
}
