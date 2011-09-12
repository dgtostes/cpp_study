/*
http://www.python.org.br/wiki/EstruturaSequencial
02
*/

#include <iostream>
#include <string>

using namespace std;

int recieve_and_return()
{
    int number;
    cout << "input a number --> " ;
    cin >> number;
    return number;
}


int main()
{
    cout << "the number inputed was ---> " << recieve_and_return() << "\n\n";
    return 0;
}

