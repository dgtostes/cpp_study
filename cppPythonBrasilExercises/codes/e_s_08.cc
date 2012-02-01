/*
http://www.python.org.br/wiki/EstruturaSequencial
08
*/
#include <iostream>
#include <string>

using namespace std;

float number_hours()
{
	float number_h; 
	cout << "input the number of hours worked in this month --> ";
	cin >> number_h;
	return number_h;
}

float salary_per_hour()
{
	float salary_per_h; 
	cout << "input your salary per hour worked --> ";
	cin >> salary_per_h;
	return salary_per_h;
}

float salary(float number_h, float salary_per_h)
{
	return salary_per_h*number_h;
}

int main()
{
	cout << "your salary is $ --> " << salary(number_hours(), salary_per_hour()) << "\n\n";
}
