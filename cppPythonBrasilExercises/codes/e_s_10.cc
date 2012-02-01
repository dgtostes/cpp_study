/*
http://www.python.org.br/wiki/EstruturaSequencial
10
*/
#include <iostream>
#include <string>

using namespace std;

float celsius_2_farenheit(float temp_celsius)
{
	float temp_farenheit;
	temp_farenheit = ((temp_celsius*9)/5)+32;
	return temp_farenheit;
}

int interaction()
{
	float temp_celsius;
	cout << "input a celcius temp --> ";
	cin >> temp_celsius;
	cout << "farenheit temp --> " << celsius_2_farenheit(temp_celsius) << "\n\n";
	return 0;	
}

int main()
{
	interaction();
	return 0;
}
