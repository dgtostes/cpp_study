/*
http://www.python.org.br/wiki/EstruturaSequencial
01
*/

#include <iostream>
#include <string>

using namespace std;


float avg()
{
	float sum = 0;
	float score, avg_score, float_i;
	int i;
	for(i = 1; i < 5; i = i + 1)
	{
		cout << "input the score of the test " << i << " ---> ";
		cin >> score;
		sum = sum + score;
	}
	float_i = (float)i - 1;
	avg_score = sum/float_i;
	return avg_score;

}


int main()
{
	cout << "the avg test score is --> " << avg() << "\n\n";
}
