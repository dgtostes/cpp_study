/*
http://www.python.org.br/wiki/EstruturaSequencial
07
*/
#include <iostream>
#include <string>

using namespace std;

float square_area(float side)
{
	return side*side;
}

int interaction()
{
	float side;
	float square_area_value;
	cout << "input a side unit --> ";
	cin >> side;
	square_area_value = square_area(side);
	cout << square_area_value << " area units\n";
	cout << 2*square_area_value << " is double of area units\n\n";
	return 0;
}

int main()
{
	interaction();
}
