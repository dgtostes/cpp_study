#include <iostream>
#include <string>

using namespace std;

int main(){
	//std::cout << "Hello, world\n";
	int i = 0;
	for(i; i<10; i = i + 1){
		if(i == 2){
			cout << "pulão!!!\n\a";		
		}
		else{
			cout << i <<"\n";
		}

	}
	int x, y;
	x = 4 + 2;
	cout << x/3 <<  ' ' << x*2 << "\n";

	cout << "digite um numero ---> ";
	cin >> y;

	cout << "número digitado --> " << y << "\n";
	
	return 0;

}
