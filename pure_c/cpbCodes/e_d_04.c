#include <stdio.h>
#include <string.h>

main()
{
	char *a[10];
	int i;

	a[0] = "a";
	a[1] = "e";
	a[2] = "i";
	a[3] = "o";
	a[4] = "u";
	a[5] = "A";
	a[6] = "E";
	a[7] = "I";
	a[8] = "O";
	a[9] = "U";


	char let[1];
	puts("inputa leter --> ");
	gets(let);

	int ver;
	ver = 0;

	int comp;

	for(i=0; i<10; i++)
	{


		comp = strncmp(let, a[1],1);
		printf("-------------------->%d\n\n", comp);
		
		if(comp == 0) 
		{

			ver = 1;
			puts("\tentrou \n\n\n\n");
			break;
		}
	}


	printf("\n\n%d\n\n", ver);

	if(ver == 0)
	{
		puts("you inputed a consoant\n\n");
	}
	else
	{
		puts("you inputed a vogal\n\n");
	}
}
