#include <stdio.h>

float time4(float size, float speed)
{
	return size/(speed*60);
}


float ask4float(char sentence[])
{
	float variable2return;
	printf("%s", sentence);
	scanf("%f", &variable2return);
	return variable2return;
}

main()
{
	float size, speed;
	size = ask4float("input the file size --> ");
	speed = ask4float("input a speed (Mbps) --> ");
	printf("The download duaration will be --> %.2f minutes\n\n", time4(size, speed));
}
