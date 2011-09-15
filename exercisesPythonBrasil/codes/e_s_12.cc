/*
http://www.python.org.br/wiki/EstruturaSequencial
12
*/
#include <iostream>
#include <string>

using namespace std;

float ideal_weight(float height)
{
	return (72.7*height) - 58;
}

int interaction()
{
	float height;
	cout << "input your height --> ";
	cin >> height;
	cout << "your ideal weight is --> " << ideal_weight(height)  << "\n\n";
	return 0;
}


int main()
{
	interaction();
	return 0;
}
