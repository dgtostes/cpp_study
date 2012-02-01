#include <stdio.h>


int first_operaton(int number1, int number2)
{
	return number1*2*(number2/2);
}


float second_operation(int number1, float number3)
{
	return (number1*3)+number3;
}

float third_operation(float number3)
{
	return number3*number3*number3;
}


main()
{
	int number1, number2;
	float number3;
	printf("input a integer number --> ");
	scanf("%d", &number1);
        printf("input other integer number --> ");
        scanf("%d", &number2);
        printf("input a real number --> ");
        scanf("%f", &number3);
	printf("first %d\n second %f\n third %f\n\n", first_operaton(number1, number2), second_operation(number1,number3), third_operation(number3));

}

