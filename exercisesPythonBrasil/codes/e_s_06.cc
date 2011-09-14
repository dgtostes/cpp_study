/*
http://www.python.org.br/wiki/EstruturaSequencial
06
*/
#include <iostream>
#include <string>



using namespace std;

float circle_area(float radius)
{
	return 3.14*radius*radius;
}

int interaction()
{
	float radius, circle_area_value;
	cout << "input a radius unit --> ";
	cin >> radius;
	circle_area_value = circle_area(radius);
	cout << circle_area_value << " area units\n\n";
	return 0;
}

int main()
{
	interaction();
}
