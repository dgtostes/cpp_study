#include <stdio.h>

float avg(float score1, float score2, float score3, float score4)
{
	return (score1+score2+score3+score4)/4.0;
}

float get_score()
{
	float score;
	printf("input a scrore --> ");
	scanf("%.2f", &score);
	return score;
}

main()
{
	float a,b,c,d, sum;
	sum =0;
	
	printf("input a score --> ");
	scanf("%f", &a); 
	printf("input a score --> ");
	scanf("%f", &b); 
	printf("input a score --> ");
	scanf("%f", &c); 
	printf("input a score --> ");
	scanf("%f", &d); 
	printf("score avg is --> %.2f\n\n", avg(a,b,c,d));
}



