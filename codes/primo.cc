#include <iostream>
using namespace std;


bool ehprimo(int testeNumber)
{
	bool resultado;
	int divNumber;
	int verificador = 0;
	divNumber = testeNumber - 1;
	while(divNumber > 1){
		if (testeNumber%2 == 0){
			verificador = 1;
			resultado = false;
         		return resultado;
			break;
		}
		else if(testeNumber%divNumber == 0){
			resultado = false;
		        return resultado;
			break;
		}
		divNumber = divNumber - 1;
	}
	if(verificador == 0){
		resultado = true;
		return resultado;
	}
}

int main(){

	int interacoes;
	cout << "numero de interacoes --> ";
	cin >> interacoes;
	
	for(int numero = 3; numero <= interacoes; numero ++){
		if(ehprimo(numero)){
			cout << numero << "\n";
		}/*
		else{
			cout << numero << " nao eh primo\n";
		}*/
	}
}
