/*
http://www.python.org.br/wiki/EstruturaSequencial
09
*/
#include <iostream>
#include <string>

using namespace std;


float farenheit_2_celsius(float temp_farenheit)
{
	float temp_celcius;
	temp_celcius = (5*(temp_farenheit-32)/9);
	return temp_celcius;
}

int interaction()
{
	float temp_farenheit;
	cout << "input a farenheit temp --> ";
	cin >> temp_farenheit;
	cout << "celsius temp --> " << farenheit_2_celsius(temp_farenheit) << "\n\n";
	return 0;	
}

int main()
{
	interaction();
	return 0;
}
