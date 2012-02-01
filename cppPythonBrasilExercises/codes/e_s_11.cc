/*
http://www.python.org.br/wiki/EstruturaSequencial
11
*/
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

float operation1(float number1, float number2)
{
	return (number1*2)*(number2/2);
}

float operation2(float number1, float number2)
{
	return (number1*3)+number2;
}

float operation3(float number1)
{
	return pow(number1,3);
}

int interaction()
{
	int number1, number2;
	float number3;
	cout << "input a number --> ";
	cin >> number1;
	cout << "input other number --> ";
	cin >> number2;
	cout << "input other number --> ";
	cin >> number3;
	cout << "operation 1 --> " << operation1((float)number1, (float)number2) << "\n";
	cout << "operation 2 --> " << operation2((float)number1, (float)number3) << "\n";
	cout << "operation 3 --> " << operation3(number3) << "\n\n";
	return 0;
}

int main()
{
	interaction();
	return 0;
}
