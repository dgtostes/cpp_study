/*
http://www.python.org.br/wiki/EstruturaSequencial
05
*/
#include <iostream>
#include <string>

using namespace std;

float m_2_cm(float meters)
{
	return meters*100;
}

int interaction()
{
	float meter;
	cout << "input a meter unit --> ";
	cin >> meter;
	cout << meter << " m equals " << m_2_cm(meter) << " cm\n\n";
	return 0;
}


int main()
{
	interaction();
}

