#include <stdio.h>
#include "dgt_lib.h"


int verify_sex(char sex[])
{
	if(sex == "M")
	{
		puts("Male\n");
	}
	else
	{
		puts("Female\n");
	}
	return 0;
}

main()
{
	char sex;
	puts("input your sex (M)ale (F)emale ---> ");
	scanf("%c", &sex);
	verify_sex(sex);
