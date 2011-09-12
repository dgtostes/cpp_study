/*
http://www.python.org.br/wiki/EstruturaSequencial
03
*/

#include <iostream>
#include <string>

using namespace std;

float sum(float number1, float number2)
{
	float result = number1 + number2;
	return result;
}

float interaction()
{
	float number1, number2;	
	cout << "input a number ---> ";
	cin >> number1;
	cout << "input another number ---> ";
	cin >> number2;
	return sum(number1,number2);
		
}

int main()
{
	cout << "the sum of the inputed number is ---> " << interaction() << "\n\n";
	return 0;
}
